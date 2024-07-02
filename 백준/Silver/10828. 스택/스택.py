# 문제를 잘 읽자.
import sys
input=sys.stdin.readline

N= int(input())
Stack = []

for _ in range(N):
    M = input().strip()
    if M.startswith("push") :
        number = [int(n) for n in M if n.isdigit()]
        num = ''.join(str(num) for num in number)
        M = "push"
        # print("num: " , num)
        Stack.append(num)
    # print("M :" , M)
    elif M == "pop" :
        if Stack == [] :
            print(-1)
        else :
            k = Stack.pop()
            print(k)
    elif M == "size" :
        print(len(Stack))
    elif M == "empty" :
        if Stack == [] :
            print(1)
        else :
            print(0)
    else :
        if Stack == [] :
            print(-1)
        else :
            print(Stack[-1]) 