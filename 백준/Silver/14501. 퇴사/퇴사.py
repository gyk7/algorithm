N = int(input())
T = []
P = []
max_price = [0] * (N+1)

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N-1, -1, -1):
    if T[i] + i > N : # 상담이 퇴사일을 넘기면 진행하지 않음.
        max_price[i] = max_price[i+1]
    else:
        max_price[i] = max(max_price[i+1], P[i] + max_price[i + T[i]])
print(max_price[0])