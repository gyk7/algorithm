N, K = map(int, input().split())
li = []
cnt = 0

for _ in range(N):
    A = int(input())
    li.append(A)
li.sort(reverse=True)

for i in li :
    if i <= K :
        cnt += K // i
        K = K % i
        if K == 0 :
            break
        else :
            continue

print(cnt)