N = int(input())

# dp[] table 정의
dp = [0] * (N+1)

# dp[]의 초기값 설정
dp[0], dp[1] = 1, 1

# 범위 정해서 반복처리
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

ans = dp[N]
print(ans  % 10007)