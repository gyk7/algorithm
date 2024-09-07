N = int(input())
arr = []

for i in range(N) :
    li = list(map(int, input().split()))
    arr.append(li)
dp = arr

# print(arr)
for i in range(1, N) :
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
# print(dp)
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))