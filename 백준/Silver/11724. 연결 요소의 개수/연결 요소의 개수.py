N, M= map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0
for _ in range(M):
    p, q = map(int,input().split())
    
    graph[p][q] = graph[q][p] = 1

# print(graph)
def bfs(V):
    visited[V] = 1
    deque=[V]    
    while deque:
        # print(deque)
        V = deque.pop(0)
        # print(V, end=' ')
        
        for i in range(1, N+1):
            if graph[V][i] ==1 and visited[i] == 0:
                deque.append(i)
                visited[i] = 1




for j in range(1, N+1) :
    if visited[j] == 0 :
        bfs(j)
        cnt +=1
        # print(f'#########{j}')
print(cnt)