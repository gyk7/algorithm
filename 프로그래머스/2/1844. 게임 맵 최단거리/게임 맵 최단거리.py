from collections import deque

def solution(maps):
    answer = 0
    
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]

    # 세로길이
    n = len(maps)
    
    # 가로길이
    m = len(maps[0])

    
    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q :
            x, y = q.popleft()
            
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0<= ny < m and maps[nx][ny] == 1 :
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
        if maps[n-1][m-1] == 1 :
            return -1
        
        return maps[n-1][m-1]
            
        
    return bfs(0,0)