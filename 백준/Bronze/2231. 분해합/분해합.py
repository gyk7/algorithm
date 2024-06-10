N = int(input())

for i in range(N) :
    s = i + sum(map(int, str(i)))

    if s == N :
        print(i)
        break

else :
    print(0)