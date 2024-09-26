from collections import deque

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(y,x) :
    deq = deque()
    deq.append((y,x))
    graph[y][x] = 0
    cnt = 0
    
    while deq :
        y, x = deq.popleft()
        cnt += 1
        for dx, dy in d :
            Y, X = y+ dy, x + dx
            if 0<= Y <n and 0<=X<m and graph[Y][X] == 1 :
                graph[Y][X] = 0
                deq.append((Y, X))
    
    return cnt



result = 1
for y in range(n) :
    for x in range(m) :
        if graph[y][x] == 1 :
            result = max(result, bfs(y,x) )

print(result)