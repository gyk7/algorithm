import collections

def solution(nums):
    d = collections.Counter(nums)

    li = [k for k, v in d.items()]
    
    if len(li) >= len(nums)/2 :
        return len(nums) / 2
    else :
        return len(li)
