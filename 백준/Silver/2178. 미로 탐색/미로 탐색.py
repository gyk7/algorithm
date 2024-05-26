from collections import deque

N, M = map(int, input().split())
graph = []
visited = [[0]*M for _ in range(N)]
for _ in range(N):
    k = list(map(int,input()))
    graph.append(k)
# print(graph)
# print(visited)

def bfs():
    # 상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append((0, 0))
    while queue : 
        x, y = queue.popleft()   
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # print(f"테스트 : {nx} {ny} ")
            if nx < N and nx >= 0 and ny < M and ny >= 0 and graph[nx][ny] == 1 and visited[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = 1
                queue.append((nx, ny))
                
    return graph[N-1][M-1]

print(bfs())