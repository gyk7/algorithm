li = []
N, M = map(int, input().split())

num = input().split()

for i in range(N):
    num[i] = int(num[i])

# print(num)

for j in range(N):
    for k in range(j+1, N):
        for l in range(k+1, N):
            s = num[j] + num[k] + num[l]
            li.append(s)
li = list(set(li))

# remove는 원본 리스트에 손상을 입히므로 리스트의 복사본을 사용해야함.
for m in li[:] :
    if m > M :
        li.remove(m)
    else:
        continue
# print(li)
print(max(li))