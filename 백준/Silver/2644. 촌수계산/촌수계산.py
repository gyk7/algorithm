import sys
sys.setrecursionlimit(10000)

n = int(input())
p, q = map(int, input().split())
m = int(input())
graph = [[0]* (n+1) for _ in range(n+1)] 
visited = [0] * (n+1)
result =[]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
# print(graph)


def dfs(V,ans):

    visited[V] = 1
    
    
    if V== q :
        print(ans)
        exit()
    for i in range(1, n+1):
        if graph[V][i] == 1 and visited[i] == 0 :
            dfs(i, ans+1)
    return -1     
   

print(dfs(p, 0))