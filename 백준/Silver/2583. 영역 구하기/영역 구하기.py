import sys
sys.setrecursionlimit(10000)

M, N, K = map(int, input().split())
graph = [[0] *  N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
   
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1

# print(graph)

dx = [0, 0, 1, -1]
dy = [1,-1, 0, 0]

def dfs(x, y, count) :
    graph[y][x] = 1
    for p in range(4) :
        nx = x + dx[p]
        ny = y + dy[p]
        if 0 <= nx < N and 0<= ny < M and graph[ny][nx] == 0 :
            count = dfs(nx, ny, count + 1)
    return count

result = []

for ny in range(M):
    for nx in range(N) :
        if graph[ny][nx] == 0:
            result.append(dfs(nx, ny, 1))

print(len(result))
print(*sorted(result))