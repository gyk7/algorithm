# 백준 11279번
import sys
import heapq

N = int(sys.stdin.readline())
heap = []
result = []

for i in range(N) :
    data = int(sys.stdin.readline())
    if data == 0 :
        if not heap:
            result.append(0)
        else :
            result.append(-heapq.heappop(heap))
    else :
        heapq.heappush(heap,-data)
print("\n".join(map(str,result)))