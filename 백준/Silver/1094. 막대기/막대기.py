X = int(input())

n = 64
num = 0

while X != 0 :
    if X >= n : 
        X -= n
        num += 1
    n = n // 2

print(num)