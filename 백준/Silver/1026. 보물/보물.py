N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()

sum = 0
for i in range(len(B)):
    sum += sorted(B, reverse = True)[i] * A[i] 


print(sum)