import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
tree = [[] for _ in range(n+1)]

def dfs(start, now) :
    for x, y in tree[start] :
        if visited[x] == -1 :
            visited[x] = y + now
            dfs(x, visited[x])
            
for _ in range(n-1) :
    a, b, l = map(int, input().split())
    tree[a].append([b,l])
    tree[b].append([a,l])

visited = [-1] * (n + 1)    
visited[1] = 0    
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[start] = 0
dfs(start, 0)
print(max(visited))