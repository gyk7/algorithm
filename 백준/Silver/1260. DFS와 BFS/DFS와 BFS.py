def dfs(c) :
    visited_dfs[c] = 1
    ans_dfs.append(c)
    for n in adj[c] :
        if visited_dfs[n] == 0 :
            dfs(n)

def bfs(s) :
    q = []
    
    q.append(s)
    ans_bfs.append(s)
    visited_bfs[s] = 1
    
    while q :
        n = q.pop(0)
        for i in adj[n] :
            if not visited_bfs[i]:
                q.append(i)
                ans_bfs.append(i)
                visited_bfs[i] = 1
            

N, M, V = map(int, input().split())
adj = [[] * (N+1) for _ in range(N + 1)]
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)
ans_dfs = []
ans_bfs = []
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(1, N+1) :
    adj[i].sort()
dfs(V)
print(*ans_dfs)
bfs(V)
print(*ans_bfs)