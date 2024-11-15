T = int(input())

for test_case in range(1, T+1):
    ans = []
    li = [0] * 5001
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            li[i] +=1
    P = int(input())
    for _ in range(P):
        C = int(input())
        ans.append(li[C])
    print(f'#{test_case}', *ans) 