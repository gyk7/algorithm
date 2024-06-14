def solution(clothes):
    hashmap = {}
    result = 1
    
    for name, type in clothes :
        hashmap[type] = hashmap.get(type, 0) + 1
    
    for type in hashmap :
        result *= (int(hashmap[type]) + 1)
    
    result -= 1    
    return result