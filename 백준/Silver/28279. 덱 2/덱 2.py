from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deq = deque()

for _ in range(N) :
    command = input().strip()
    if command[0] == '1' :
        deq.appendleft(int(command[2:]))
    
    elif command[0] == '2' :
        deq.append(int(command[2:]))
    
    elif command[0] == '3' :
        if len(deq) == 0 :
            print(-1)
        else :
            k = deq.popleft()
            print(k)
    elif command[0] == '4' :
        if len(deq) == 0 :
            print(-1)
        else :
            r = deq.pop()
            print(r)
    elif command[0] == '5' :
        print(len(deq))
    elif command[0] == '6' :
        if len(deq) == 0 :
            print(1)
        else :
            print(0)
    elif command[0] == '7' :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[0])
    elif command[0] == '8' :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[-1])

    