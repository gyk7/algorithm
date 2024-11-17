
T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())
    arr=[[0]*(N+1) for _ in range(N+1)]
    arr[N//2+1][N//2+1] = 2
    arr[N//2+1][N//2] = 1
    arr[N//2][N//2+1] = 1
    arr[N//2][N//2] =2


    for _ in range(M):
        p, q, c = map(int, input().split())
        arr[p][q] = c
        for di, dj in ((-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1),(0,-1),(0,1)):
            r = []
            for mul in range(1, N):
                ni = p + mul * di
                nj = q + mul * dj
            
                if 1<=ni<=N and 1<=nj<=N :
                    if arr[ni][nj] == 0 :
                        break
                    elif arr[ni][nj] == c:
                        while r :
                            a, b = r.pop()
                            arr[a][b]=c
                        break
                    else :
                        r.append((ni,nj))
                else:
                    break
    bcnt = 0
    wcnt = 0
        
    for lst in arr :
        bcnt += lst.count(1)
        wcnt += lst.count(2)
        
    print(f'#{test_case} {bcnt} {wcnt}')
