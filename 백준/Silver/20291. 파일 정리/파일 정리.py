N = int(input())

a = []
b = []
for _ in range(N):
    a.append(input().split('.'))

# print(a)

for i in range(N):
    b.append(a[i][1])
b.sort()
dict ={}
for num in b :
    if num in dict :
        dict[num] += 1
    else :
        dict[num] = 1

for k in dict :
    print(k, dict[k])
