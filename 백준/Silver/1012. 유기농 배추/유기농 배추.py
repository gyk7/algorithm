
T = int(input())

def bfs(x, y) :
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    queue = [(x,y)]
    graph[x][y] = 0

    while queue:
        x,y = queue.pop(0)

        
        # print(j)
        for p in range(4) :
            nx = x + dx[p]
            ny = y + dy[p]            
            

            if nx >= 0 and nx < M and ny >= 0 and ny < N and graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]=0
        

            
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * N for l in range(M)]

    cnt = 0
    for i in range(K):
        X, Y = map(int, input().split())
        graph[X][Y] = 1
    
    
    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1 :
                bfs(a,b)
                cnt += 1
    # print(graph)
    print(cnt)


    

