N, M = map(int,input().split())
line_n = int(input())
width = []
height = []
a = []
b = []

for i in range(line_n) :
    p, q = map(int, input().split())

    if p == 0 :
        height.append(q)
    if p == 1 :
        width.append(q)
height.append(0)
height.append(M)
width.append(0)
width.append(N)
height.sort()
width.sort()

for j in range(len(height) - 1) :
    a.append(height[j+1] - height[j])

for k in range(len(width) - 1) :
    b.append(width[k+1] - width[k])
    
# print(a)
# print(b)

print(max(a) * max(b))