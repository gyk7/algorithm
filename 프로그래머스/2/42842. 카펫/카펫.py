def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow + 1) :
        if yellow % i == 0 :
            j = yellow / i
            if i >= j and (i+j) * 2 + 4 == brown :
                return [i+2, j+2]