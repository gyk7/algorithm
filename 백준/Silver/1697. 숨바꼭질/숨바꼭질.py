def bfs(s, e) :
    q = []
    q.append(s)
    v[s] = 1
    while q :
        i = q.pop(0)
        
        if i == e :
            return v[e]-1
        for n in (i-1, i+1, i*2):
            if 0<= n < 200000 and v[n] == 0 :
                q.append(n)
                v[n] = v[i] + 1
    return -1  
N, K = map(int,input().split())
v = [0] * 200000
print(bfs(N, K))