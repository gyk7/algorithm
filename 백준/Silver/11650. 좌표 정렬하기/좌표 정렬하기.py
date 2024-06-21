N = int(input())

li = []

for _ in range(N) :
    x, y = map(int, input().split())
    li.append((x, y))

li.sort()
# print(li)
for i in range(N) :
    print(li[i][0], li[i][1])