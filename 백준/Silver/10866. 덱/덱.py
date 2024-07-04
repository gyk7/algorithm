from collections import deque
import sys
input= sys.stdin.readline

N = int(input())
deque = deque()

for _ in range(N) :
    command = input().strip()
    
    if command[:10] == 'push_front' :
        deque.appendleft(command[11:])
    elif command[:9] == 'push_back' :
        deque.append(command[10:])
    elif command == 'pop_front':
        if len(deque) == 0 :
            print(-1)
        else :
            k = deque.popleft()
            print(k)
    elif command == 'pop_back':
        if len(deque) == 0 :
            print(-1)
        else :
            k = deque.pop()
            print(k)
    elif command == 'size' :
        print(len(deque))
    elif command == 'empty':
        if len(deque) == 0 :
            print(1)
        else :
            print(0)
    elif command == 'front' :
        if len(deque) == 0 :
            print(-1)
        else :
            print(deque[0])
    elif command == 'back' :
        if len(deque) == 0 :
            print(-1)
        else :
            print(deque[-1])