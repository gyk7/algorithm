N, M = map(int,input().split())

li = []

def dfs(start) :
    if len(li) == M :
        print(' '.join(map(str, li)))
        return
    for i in range(start, N + 1) :
        li.append(i)
        dfs(i)
        li.pop()
        
dfs(1)