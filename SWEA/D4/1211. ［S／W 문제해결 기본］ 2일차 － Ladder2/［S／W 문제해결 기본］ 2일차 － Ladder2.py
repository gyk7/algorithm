for test_case in range(10) :
    n = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    dr = 0
    mn = 100 * 100
    for sj in range(1, 101):
        if arr[0][sj] == 0 :
            continue
        ci = 0
        cj=sj
        cnt = 0
        dr = 0
        while ci <99 :
            cnt += 1
            if dr == 0 :
                ci += 1
                if arr[ci][cj-1]==1 :
                    dr = -1
                elif arr[ci][cj+1]==1 :
                    dr = 1
            else : # 좌우
                cj += dr
                if arr[ci][cj+dr] == 0 :
                    dr = 0
        if mn >= cnt :
            mn, ans = cnt, sj-1 
               
    print(f"#{n} {ans}")