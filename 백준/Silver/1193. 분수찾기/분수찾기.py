X = int(input())

line = 1

sum = 0

while line < X :
    X -= line
    line += 1
# print(line)
for i in range(1, line):
        sum += i

if line % 2 == 0 :
   print(f"{X}/{line-X+1}")
else :
    print(f"{line-X+1}/{X}")