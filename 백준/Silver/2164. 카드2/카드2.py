import sys
from collections import deque 
input = sys.stdin.readline

N = int(input())

Queue = deque()

for i in range(1, N+1):
    Queue.append(i)
 # print(Queue)
while len(Queue) != 1 :
    del Queue[0]
    k = Queue.popleft()
    # print("k",k)
    Queue.append(k)
    # print(Queue)
print(*Queue)