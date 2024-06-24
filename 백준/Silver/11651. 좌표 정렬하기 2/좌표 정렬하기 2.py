N = int(input())
li = []

for _ in range(N) :
    x, y = map(int, input().split())
    li.append([x, y])

li = sorted(li, key = lambda x:(x[1], x[0]))

for i in range(N):
    print(li[i][0], li[i][1])