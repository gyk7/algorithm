# 다시
import sys
sys.setrecursionlimit(100000) 

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(1, N):
    p, q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)            
    
def dfs(v):

    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(i)
   
dfs(1)

for i in range(2, N+1):
    print(visited[i])
