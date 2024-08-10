import sys
import heapq

heap = []
result = []

N = int(sys.stdin.readline())

for i in range(N):
    data = int(sys.stdin.readline())
    if data == 0 :
        if not heap :
            result.append(0)
        else:
            result.append(heapq.heappop(heap))
    else :
        heapq.heappush(heap, data)
print("\n".join(map(str,result)))