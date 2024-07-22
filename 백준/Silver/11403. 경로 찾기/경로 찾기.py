N = int(input())
graph = []
for i in range(N):
    li = list(map(int, input().split()))
    graph.append(li)    
# print(graph)

for p in range(N) :
    for q in range(N) :
        for r in range(N):
            if graph[q][p] + graph[p][r] == 2 :
                graph[q][r] = 1

for j in range(N):
    for k in range(N):
        print(graph[j][k], end = " ")
    print()