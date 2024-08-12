N, M = map(int, input().split())

nums =[i+1 for i in range(N+1)]
visited= [False] * (N + 1)

def back_tracking(arr, length, visited) :
    if length == M:
        print(*arr)
    
    for i in range(1, N + 1):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            back_tracking(arr, length + 1, visited)
            arr.pop()
            visited[i] = False

back_tracking([],0, visited)