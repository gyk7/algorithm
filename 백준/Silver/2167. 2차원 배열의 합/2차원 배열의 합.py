N, M = map(int, input().split())
li=[]
li2=[]

for _ in range(N):
    p = list(map(int,input().split()))
    li.append(p)    
# print(li)

K = int(input())
for _ in range(K):
    sum = 0
    i,j,x,y = list(map(int, input().split()))
    for t in range(i-1,x):
        for r in range(j-1, y):
            sum+=li[t][r]
    li2.append(sum)
for z in li2:
    print(z)