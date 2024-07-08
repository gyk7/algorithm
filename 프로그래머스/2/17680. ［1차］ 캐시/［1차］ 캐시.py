from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    time = 0
    
    if cacheSize < len(cities) :
        for i in cities :
            i = i.upper()
            if i not in cache :
                cache.appendleft(i)
                # print(cache)
                time += 5
            else :
                cache.remove(i)
                cache.appendleft(i)
                # print(cache)
                time += 1
    else :
        for i in cities :
            if i not in cache :
                cache.appendleft(i)
                time += 5
            else :
                cache.remove(i)
                cache.appendleft(i)
                time +=1
    return time