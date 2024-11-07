T= int(input())
di = [0,1,0,-1]
dj = [1,0,-1,0]

for test_case in range(1, T+1):
    N = int(input())
    snail =[[0]*N for _ in range(N)]
    
    # 초기화
    i=0 
    j=0
    dr = 0
    cnt = 1
    
    snail[i][j] = cnt
    cnt += 1

    while cnt <= N * N :
        ni = i + di[dr]
        nj = j + dj[dr]
        
        if 0<=ni<N and 0<=nj<N and snail[ni][nj]==0:
            i = ni
            j = nj
            snail[i][j]=cnt
            cnt += 1
        else :
            dr = (dr + 1) % 4
 
    print(f"#{test_case}")
    for row in snail:
        print(*row)