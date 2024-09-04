N, M = map(int, input().split())
J = int(input())
current = 1
ans = 0

for i in range(J) :
    p = int(input())
    
    if current <= p < current + M - 1 :
        continue
    elif p > current :
        ans += p - current - (M - 1)
        current += p - current - (M - 1)
    else :
        ans += current - p 
        current -= current - p

print(ans)