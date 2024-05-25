N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
visited1 = [0] * (N+1)
visited2 = [0] * (N+1)
for _ in range(M):
    p, q = map(int,input().split())
    
    graph[p][q] = graph[q][p] = 1

def dfs(V):
    visited1[V] = 1

    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

def bfs(V):
    visited2[V] = 1
    deque=[V]
    while deque:
        V = deque.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if graph[V][i] ==1 and visited2[i] == 0:
                deque.append(i)
                visited2[i] = 1
        

  
dfs(V)
print()
bfs(V)