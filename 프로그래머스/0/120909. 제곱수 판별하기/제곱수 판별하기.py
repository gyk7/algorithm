def solution(n):
    answer = 0
    
    for i in range(1, 1001) :
        if i * i == n :
            answer = 1
            break
        else :
            answer = 2
    return answer