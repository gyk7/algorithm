k = int(input())
li = list(map(int, input().split()))
arr = [[] for _ in range(k)]

def seperation(li, depth):
    if len(li) == 1 :
        arr[depth].extend(li)
        return
    
    mid = len(li) // 2
    arr[depth].append(li[mid])
    seperation(li[:mid], depth + 1)
    seperation(li[mid + 1 :], depth + 1)

seperation(li, 0)

for i in arr :
    for j in i :
        print(j, end = " ")
    print()