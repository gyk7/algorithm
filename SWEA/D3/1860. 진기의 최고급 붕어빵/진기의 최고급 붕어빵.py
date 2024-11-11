T = int(input())

for test_case in range(1, T+1) :
    N, M, K = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort()
    answer = 'Possible'
    cnt = 0
    for i in li :
        cnt += 1
        if (i // M) * K < cnt :
            answer = 'Impossible'
            break
    print(f"#{test_case} {answer}")