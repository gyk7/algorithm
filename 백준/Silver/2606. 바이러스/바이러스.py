def dfs(si) :
    global ans
    
    ans += 1
    v[si] = 1
    for se in adj[si] :
        if not v[se] : 
            dfs(se)
    return ans
N = int(input())
M = int(input())
adj = [[] * (N+1) for _ in range(N+1)]
for _ in range(M) :
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

v = [0] * (N + 1)
ans = 0
dfs(1)
print(ans - 1)