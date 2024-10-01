a = int(input())

b = 1000 - a

c = b // 500 
d = (b % 500) // 100
e = (b % 100) // 50
f = (b % 50) // 10
g = (b % 10) // 5
h = b % 5

print(c + d + e + f + g + h)