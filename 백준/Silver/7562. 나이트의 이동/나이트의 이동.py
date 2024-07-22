from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q :
        
        x, y = q.popleft()
        
        if x == x2 and y == y2 :
            return graph[x2][y2]
        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < I and 0 <= ny < I and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
                # print(q)
  
test_case = int(input())
for i in range(1, test_case + 1) :
    I = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    graph = [[0] * I for _ in range(I)]
    graph[x1][y1] = 0
    
    dx = [2,2,1,1,-2,-2,-1,-1]
    dy = [1,-1,2,-2,1,-1,2,-2]
    
    print(bfs(x1, y1))    