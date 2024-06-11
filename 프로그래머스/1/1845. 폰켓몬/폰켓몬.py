import collections
def solution(nums):
    d = collections.Counter(nums)
    
    list = [k for k, v in d.items()]
    
    if len(list) >= len(nums) / 2 :
        return len(nums) / 2
    else :
        return len(list)