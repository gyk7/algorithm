from collections import deque
def bfs(si, sj, sk) :
    q = deque()
    v = [[[0]*M for _ in range(N)] for _ in range(H)]

    cnt = 0
    for h in range(H) :
        for i in range(N) :
            for j in range(M) :
                if arr[h][i][j] ==1 :
                    q.append((h, i, j))
                    v[h][i][j] =1
                elif arr[h][i][j]==0 :
                    cnt += 1
    
    while q :
        ci, cj, ck = q.popleft()
        
        
        for di, dj, dk in ((-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1)) :
            ni, nj, nk = ci + di, cj + dj, ck + dk
            
            if 0<=ni<H and 0<=nj<N and 0<=nk<M and arr[ni][nj][nk] == 0 and v[ni][nj][nk] == 0 :
                q.append((ni, nj, nk))
                v[ni][nj][nk] = v[ci][cj][ck] + 1
                cnt -= 1
    if cnt == 0 :
        return v[ci][cj][ck] - 1
    else :        
        return -1                   


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = bfs(0, 0, 0)
print(ans)