def solution(answers):
    list = []
    answer = []
    sum1 = 0
    sum2 = 0
    sum3 = 0
    
    people1 = [1,2,3,4,5]
    people2 = [2,1,2,3,2,4,2,5]
    people3 = [3,3,1,1,2,2,4,4,5,5] 
    
    for i in range(len(answers)) :
        if answers[i] == people1[i % 5] :
            sum1 += 1
        if answers[i] == people2[i % 8] :
            sum2 += 1
        if answers[i] == people3[i % 10] :
            sum3 += 1
            
    list.append(sum1)
    list.append(sum2)
    list.append(sum3)
    
    if list.count(max(list)) >= 2 :
        return [i + 1 for i, v in enumerate(list) if v == max(list)]
    else :
        return [list.index(max(list)) + 1]
