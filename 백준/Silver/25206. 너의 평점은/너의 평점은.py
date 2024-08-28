result = 0
sum = 0
for _ in range(20) :
    K= input()
    K = K.split(" ")
    
    subject = K[0]
    score = float(K[1])
    grade = K[2]

    if grade == 'A+' :
        avscore = 4.5
    elif grade == 'A0' :
        avscore = 4.0
    elif grade == 'B+' :
        avscore = 3.5
    elif grade == 'B0' :
        avscore = 3.0
    elif grade == 'C+' :
        avscore = 2.5
    elif grade == 'C0' :
        avscore = 2.0
    elif grade == 'D+' :
        avscore = 1.5
    elif grade == 'D0' :
        avscore = 1.0 
    elif grade == 'F' :
        avscore = 0.0
    

    if grade != 'P':
        sum += score
        result += score * avscore
result = result / sum
print(result)