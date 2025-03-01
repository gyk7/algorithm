N = int(input())
T = [0] * N
P = [0] * N

for i in range(N) :
    T[i], P[i] = map(int, input().split())

dp = [0] * (N+1)
for n in range(N-1, -1, -1) :   # 뒤에서 앞으로(완료기준)
    if n + T[n] <= N :          # 기간 내 상담완료 가능
        dp[n] = max(dp[n+T[n]]+P[n], dp[n+1])
    else :
        dp[n] = dp[n+1]
print(dp[0])