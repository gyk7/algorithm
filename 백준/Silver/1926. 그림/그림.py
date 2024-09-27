import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = []

for i in range(n) :
    k = list(map(int, input().split()))
    graph.append(k)

# print(graph)
visited = [[0] * m for _ in range(n)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(x, y) :
    global cnt
    cnt += 1
    for dx, dy in d :
        X, Y = x + dx, y + dy
        if 0<=X<n and 0<=Y<m :
            if graph[X][Y] == 1 and visited[X][Y] == 0:
                visited[X][Y] = 1
                dfs(X, Y)

result = []
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 and visited[i][j] == 0 :
            visited[i][j] = 1
            cnt = 0
            dfs(i,j)
            result.append(cnt)

if len(result) != 0 :
    print(len(result))
    print(max(result))
else :
    print(0)
    print(0)

