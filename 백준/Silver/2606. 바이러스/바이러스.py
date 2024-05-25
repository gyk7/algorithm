N = int(input())
M = int(input())

graph_1 =[[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    p, q = map(int, input().split())
    graph_1[p][q] = 1
    graph_1[q][p] = 1
li =[1]
visited[1] = 1
cnt = 0
while li:
    V = li.pop(0)
    for i in range(1, N+1):
        if graph_1[V][i] == 1 and visited[i] == 0 :
            li.append(i)
            visited[i] = 1
            cnt+=1
print(cnt)
            