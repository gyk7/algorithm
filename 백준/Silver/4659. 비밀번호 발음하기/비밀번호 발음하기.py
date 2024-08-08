import sys

while True :
    password = sys.stdin.readline().strip()
    
    if password =='end':
        break
    
    flag = True
    
    if len(set(['a','e','i','o','u']).intersection(set(list(password)))) == 0 :
        flag = False
        
    arr = []
    for i in password:
        if i in "aeiou":
            arr.append('모음')
        else :
            arr.append('자음')
            
    
    for i in range(1, len(arr)-1):
        if arr[i-1] == arr[i] == arr[i+1] :
            flag = False
            break
    
    for j in range(len(password)-1):
        if password[j] == 'e' and password[j+1] == 'e' :
            flag = flag
        elif password[j] == 'o' and password[j+1] == 'o' :
            flag = flag
        elif password[j] == password[j+1] :
            flag = False
            break

    if flag == True :
        print("<" + f"{password}" + ">" + " is acceptable.")
    else :
        print("<" + f"{password}" + ">" + " is not acceptable.")
