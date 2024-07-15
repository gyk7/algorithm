from collections import deque
N, K = map(int, input().split())
visited = [0] * 100001
def bfs():
    queue = deque()
    queue.append((0, N)) # 소요시간, 언니의 위치
    visited[N] = 1
    while queue:
        time, c = queue.popleft()
        if c == K :
            print(time)
            break
        else :
            li = [c * 2, c + 1, c - 1]
            for i in li :
                if i >= 0 and i <= 100000:
                    if not visited[i] :
                        visited[i] = 1
                        queue.append((time+1, i))
                        # print(queue)
if N == K :
    print(0)
elif N > K :
    print(N-K)
else :
    bfs()