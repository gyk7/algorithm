def dfs(n, lst) :
    if n > N :
        if len(lst) == M :
            ans.append(lst)
        return
    
    dfs(n+1, lst + [n]) # 포함하는 경우
    dfs(n+1, lst)   # 포함하지 않는 경우

N, M = map(int, input().split())
ans = []
dfs(1,[])
for lst in ans :
    print(*lst)