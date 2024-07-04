## 다시보기
n = int(input())

Stack = []
calcu = []
cur = 1

for _ in range(0, n) :
    k = int(input())
    
    while k >= cur :
        calcu.append('+')
        Stack.append(cur)
        cur += 1
     
    if Stack[-1] == k:
        calcu.append('-')
        Stack.pop()
        
    else :
        calcu.clear()
        calcu.append('NO')
        break
    
for p in range(len(calcu)):
    print(calcu[p])