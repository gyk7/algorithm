from collections import deque

N = int(input())

q = deque()
for i in range(1, N+1) :
    q.append(i)
li = []
while len(q) > 1 :
    x = q.popleft()
    li.append(x)
    q.append(q[0])
    q.popleft()
li.append(q[0])


print(*li)