N = int(input())
M = str(N)
li = []

for i in range(len(M)):
    li.append(int(M[i]))
li.sort(reverse=True)

for j in range(len(M)):
     print(li[j], end="")    