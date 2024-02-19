list = []
sum = 0
for i in range(5):
    a = int(input())
    list.append(a)
list.sort()
for i in range(5):
    sum += list[i]

print(int(sum/5))
print(list[2])