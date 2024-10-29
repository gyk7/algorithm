def dfs(n, sum) :
    global ans
    if n == N :
        if sum == S :
            ans += 1          
        return
     
    dfs(n+1, sum + arr[n])
        
    dfs(n+1, sum)
        

N, S = map(int, input().split())
arr = list(map(int, input().split()))
v = [0] * N
ans = 0
dfs(0, 0)

if S == 0 :
    ans -= 1
print(ans)