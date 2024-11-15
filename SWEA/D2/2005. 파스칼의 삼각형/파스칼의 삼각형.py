T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    li=[[1]*i for i in range(1, N+1)]
    for j in range(0, N-1):
        for r in range(0, j):
            li[j+1][r+1] = li[j][r]+li[j][r+1]
    print(f'#{test_case}')
    for row in li :
        print(*row)
        
    