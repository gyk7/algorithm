#import sys
#sys.stdin = open("input(3).txt", "r")

for test_case in range(1, 11):
    li = []
 
    N = int(input())
    col = 0
    row = 0
    left = 0
    right = 0
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr1 = list(map(list, zip(*arr)))
    for j in range(100) :
        row = sum(arr[j])
        li.append(row)
    for i in range(100) :
        col = sum(arr1[i])
        li.append(col)
        
    for i in range(100) :
        left += arr[i][i]
    li.append(left)
    
    for i in range(100) :
        right += arr[i][99-i]
    li.append(right)
    print(f"#{N} {max(li)}")