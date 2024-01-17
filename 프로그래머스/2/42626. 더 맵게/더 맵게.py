import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville) >= 2 :
        min_ = heapq.heappop(scoville)
        if min_ >= K :
            count = count
        else :
            min2_ = heapq.heappop(scoville)
            heapq.heappush(scoville, min_+min2_*2)
            count += 1
    
    if scoville[0] < K :
        return -1
    else :
        return count