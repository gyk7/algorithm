
for test_case in range(1, 11):
    _ = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    li = [list(x) for x in zip(*arr)]
    ans = 0

    for lst in li :
        prev = 0
        for n in lst :
            if n :
                if n==2 and prev==1 :
                    ans += 1
                prev = n
                        
    print(f"#{test_case} {ans}")