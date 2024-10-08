def solution(genres, plays):
    
    answer = []
    
    dict1 = {}
    dict2 = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)) :
        if genre not in dict1 :
            dict1[genre] =[(i,play)]
        else :
            dict1[genre].append((i, play))
            
        if genre not in dict2 :
            dict2[genre] = play
        else :
            dict2[genre] += play
            
    for (k, v) in sorted(dict2.items(), key = lambda x:x[1], reverse = True):
        for (i, p) in sorted(dict1[k], key = lambda x:x[1], reverse = True)[:2]:
            answer.append(i)
            
    return answer
    
                
    