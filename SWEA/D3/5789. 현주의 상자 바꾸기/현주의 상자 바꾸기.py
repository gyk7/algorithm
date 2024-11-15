T = int(input())


for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    li = [0] * (N+1)
    for i in range(1, Q+1) :
        L, R = map(int, input().split())
        for k in range(L, R+1):
            li[k] = i
    print(f'#{test_case}', *li[1:])    
        