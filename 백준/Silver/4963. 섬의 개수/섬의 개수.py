import sys
from collections import deque
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(h) ]
    dx = [ 0, 0, -1, 1, -1, -1, 1, 1 ]
    dy = [ -1, 1, 0, 0, -1, 1, -1, 1 ]
    visit = [ [False] * w for _ in range(h) ]
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == False and graph[nx][ny] == 1:
                    visit[nx][ny] = True
                    q.append((nx, ny))
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visit[i][j] == False:
                visit[i][j] = True
                bfs(i, j)
                count += 1
    print(count)