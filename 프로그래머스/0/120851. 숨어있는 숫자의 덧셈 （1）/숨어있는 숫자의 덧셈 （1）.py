def solution(my_string):
    answer = 0
    
    for i in range(len(my_string)) :
        if my_string[i] == '1' :
            answer += 1
        if my_string[i] == '2' : 
            answer += 2
        if my_string[i] == '3' : 
            answer += 3
        if my_string[i] == '4' : 
            answer += 4
        if my_string[i] == '5' : 
            answer += 5    
        if my_string[i] == '6' : 
            answer += 6
        if my_string[i] == '7' : 
            answer += 7
        if my_string[i] == '8' : 
            answer += 8
        if my_string[i] == '9' : 
            answer += 9
    return answer