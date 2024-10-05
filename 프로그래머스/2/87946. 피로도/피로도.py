from itertools import permutations
def solution(k, dungeons):
    result = []
    for i in permutations(dungeons, len(dungeons)):
        cnt = 0
        temp = k
        for essential, reduce in i:
            if temp >= essential :
                temp -= reduce
                cnt += 1
        result.append(cnt)
    return max(result)
  