
def solution(participant, completion):
    hashdict = {}
    hashsum = 0
    
    for par in participant:
        hashdict[hash(par)] = par
        hashsum += hash(par)
    
    for com in completion :
        hashsum -= hash(com)
    
    return hashdict[hashsum]