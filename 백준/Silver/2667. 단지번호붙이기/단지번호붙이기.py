from collections import deque

N = int(input())

graph = []
one_li = []
house_li = []

for _ in range(N):
    s = list(map(int,input()))
    graph.append(s)
    one_li.append([i for i, value in enumerate(s) if value == 1])
    one_li = list(one_li)
# print(one_li)

def bfs():
    dx=[0, 0, -1, 1]
    dy=[-1, 1, 0, 0]
    queue = deque()
    
    
    while len(sum(one_li, [])) != 0 : 
        # print(f"one_li : {one_li}")
        for i in range(0, N) :
            # print(f"i :{i}")
            
             
            if len(one_li[i]) != 0 :
                # print(f"len(one_li[i]):{len(one_li[i])}")
                queue.append([i, one_li[i][0]])
                
                cnt = 1
                while queue :
                    # print(f"queue : {queue}")
                    x,y = queue.popleft()
                    # print(f"x :{x}, y: {y}")
                    graph[x][y] = 0
                    if len(one_li) != 0 :
                        # print(f"one_li :{one_li}")
                        one_li[x].remove(y)
        
                   
                    # print(f"one_li : {one_li}")
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        # print(f"test {k} {nx} {ny}")
                        if nx >= 0 and nx < N and ny >= 0 and ny < N :
                            if graph[nx][ny] == 1 and [nx,ny] not in queue: 
                                queue.append([nx, ny])
                                cnt+=1
                                # print(f"cnt : {cnt}")
                        else :
                            continue
                    # print(f"{graph}")    
                house_li.append(cnt)
            house_li.sort()
        
        house = ""
        
    if len(house_li) != 0 :    
        for k in house_li:
            house = house + str(k) + "\n"
    
        
        return  str(len(house_li)) + "\n" + house.rstrip("\n")
    
    else :
        return str(0)

print(bfs())