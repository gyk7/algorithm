import sys
input = sys.stdin.readline

Stack = []

K = int(input())

sum = 0

for _ in range(K) :
    M = int(input())
    
    if M != 0 :
        Stack.append(M)
        sum += M
    else :
        sum -= Stack[-1]
        del Stack[-1]
        
    # print(Stack)    

print(sum)