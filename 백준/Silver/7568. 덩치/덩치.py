N = int(input())
li=[]


for _ in range(N):
    x, y = map(int, input().split())
    li.append([x, y])

#print(li)

for i in range(N):
    rank = 1
    for k in range(N):
        if li[i][0] < li[k][0] and li[i][1] < li[k][1] :
            rank+=1
    print(rank, end=" ")