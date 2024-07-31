N = int(input())
li1 = list(map(int, input().split()))

M = int(input())
li2 = list(map(int, input().split()))
li1.sort()
# print(li1)
for i in li2 :
    lt, rt = 0, N-1
    isExist = False
    
    while lt <= rt :
        mid = (lt + rt) //2
        if i == li1[mid]:
            isExist=True
            print(1, end = ' ')
            break
        elif i > li1[mid] :
            lt = mid + 1
        else :
            rt = mid - 1
    
    if not isExist :
        print(0, end = ' ')
