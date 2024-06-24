li = []

for _ in range(9):
    height = int(input())
    li.append(height)
li.sort()
# print(li)
sum = sum(li)


for i in range(8):
    for j in range(i+1, 9) :
       if li[i] + li[j] == sum - 100 :
           rm_set = {li[i], li[j]}

li = [k for k in li if k not in rm_set]
for k in range(7) :
    print(li[k])