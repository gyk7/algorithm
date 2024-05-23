from collections import deque


N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(M) :
    a, b = map(int, input().split())
    # deq.append((a,b))
    graph[a][b]=graph[b][a]=1

visited1 = [0] * (N+1)
visited2 = [0] * (N+1)
def dfs(V) :
    # print(visited1, V)
    visited1[V] = 1
    print(V, end= ' ')
    
    for i in range(1, N+1) :
        if graph[V][i] == 1 and visited1[i] == 0 :
            dfs(i)



def bfs(V) :
    visited2[V] = 1
    deq = deque([V])
    # print(deq)
    while deq:
        V = deq.popleft()
        print(V, end = ' ')
        for i in range(1, N+1) :
            if graph[V][i] == 1 and visited2[i] == 0 :
                # print(111111)
                deq.append(i) 
                visited2[i] = 1
dfs(V)
print()
bfs(V)