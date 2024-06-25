import sys

N = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
b_list = list(map(int, sys.stdin.readline().split()))

a_list.sort()

for b in b_list:
    low = 0
    high = N - 1

    while low <= high:
        mid = low + (high - low) // 2

        if a_list[mid] > b :
            high = mid - 1
    
        elif a_list[mid] < b :
            low = mid + 1

        else :
            low = mid
            high = mid
            break

    if low == mid and high == mid:
        print(1)
    else :
        print(0)