N = int(input())
dasom = int(input())

li=[]
cnt = 0
for _ in range(N-1):
    people_n = int(input())
    li.append(people_n)
    
if N == 1 :
    pass
else :
    while dasom <= max(li) :
        li[li.index(max(li))] -= 1
        dasom += 1
        cnt += 1

print(cnt)