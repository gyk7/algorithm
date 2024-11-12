T = int(input())

for test_case in range(1, T+1) :
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    arr =[[""] * 3 for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            arr[i][0]+= str(li[N-1-j][i])
            arr[i][1]+= str(li[N-1-i][N-1-j])
            arr[i][2]+= str(li[j][N-1-i])
    print(f'#{test_case}')
    
    for row in arr:
        print(" ".join(row))
            