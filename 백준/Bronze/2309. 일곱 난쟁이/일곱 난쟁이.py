li = []
for _ in range(9) :
    a = int(input())
    li.append(a)

sum = 0

for i in range(9):
    sum += li[i]


d_li = []
for j in range(0, 8) :
    for k in range(j+1, 9) :
        if li[j] + li[k] == sum - 100 :
            d_li = [li[j], li[k]]
li = set(li) - set(d_li)
li = list(li)
li.sort()
for p in range(7) :
    print(li[p])