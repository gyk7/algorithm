def bfs(s, e) :
    q = []
    q.append(s)
    v[s] = 1
    while q :
        c = q.pop(0)
        if c == e :
            return v[e] - 1
        for k in adj[c] :    
            if not v[k] :
                q.append(k)
                v[k] = v[c] + 1
                
    return -1
N = int(input())
P, Q = map(int, input().split())
M = int(input())
adj = [[0] *(M + 1) for _ in range(N + 1)]
v = [0] * (N + 1)
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
print(bfs(P, Q))
# print(adj)