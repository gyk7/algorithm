
n = int(input())
graph = [[0]*101 for _ in range(101)]
area = 0

for _ in range(n) :
    d1, d2 = map(int, input().split())
    for i in range(1, 11):
        for j in range(1, 11):
            graph[d1+i][d2+j] = 1
            
# for k in range(1, 100):
#     for l in range(1, 100):
#         if graph[k][l] != 0:
#             area += 1

for i in graph :
    area += i.count(1)
print(area)           