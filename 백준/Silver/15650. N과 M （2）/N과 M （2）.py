N, M = map(int, input().split())

visited = [False] * (N + 1)
result = []
result_li = []
def backtracking(result, K) :
    if K == M :
        result_li.append(sorted(result))
        return 
    for i in range(1, N+1):
        if visited[i] == False :
            result.append(i)
            visited[i] = True
            backtracking(result, K+1)
            result.pop()
            visited[i] = False
        
backtracking([], 0)

result_li = list(set(map(tuple, result_li)))

result_li.sort()

for j in result_li :
    print(" ".join(map(str, j)))