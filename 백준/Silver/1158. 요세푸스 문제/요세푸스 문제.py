from collections import deque
N, k = map(int, input().split())
li = []
queue = deque()
for j in range(1, N+1):
    queue.append(j)

# print(queue)   
for i in range(0, N) :
    
    # i= (i+1) % len(queue)
    queue.rotate(-k+1)
    q = queue.popleft()
    # print(queue)
    li.append(q)
print('<', end='')
for p in range(N-1) :
    print(li[p], end=', ')
print(li[N-1], end='')
print(">")
