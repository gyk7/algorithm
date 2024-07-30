test_case = int(input())
result = []

for _ in range(test_case) :
    N, M = map(int,input().split())
    multiply1 = 1
    multiply2 = 1
    answer = 1
    for i in range(N) :
        multiply1 *= (M - i)
        multiply2 *= (N - i)
    answer = multiply1 // multiply2
    result.append(answer)

for k in result :
    print(k)