N = int(input())

cnt = 0
r = 0

if N < 100 :
    cnt = N
else :
    cnt += 99
    a = N // 100
    
    for i in range(1, a+1):
        for j in range(0, 10):
            r = j - i 
            k = j + r
            if k >= 0 and k <= 9 and 100 * i + 10 * j + k <= N:
                cnt += 1 
print(cnt)