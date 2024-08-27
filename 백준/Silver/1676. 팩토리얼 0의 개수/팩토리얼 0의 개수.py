N = int(input())
multiplition = 1
cnt = 0
for i in range(1, N+1) :
    multiplition *= i

multiplition = list(str(multiplition))
# print(multiplition)

for i in range(len(multiplition) - 1):
    if multiplition[len(multiplition)- 1 - i] == '0' :
        cnt += 1
    else :
        break

print(cnt)