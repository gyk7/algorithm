T = int(input())

def solve() :
    for arr in li:
        if len(set(arr)) != 9 :
            return 0
    
    li1 = list(zip(*li))
    
    for arr1 in li1 :
        if len(set(arr1)) != 9 :
            return 0
    
    for i in range(0, 9, 3) :
        for j in range(0, 9, 3) :
            li2 = []
            li2 += li[i][j:j+3] + li[i+1][j:j+3] + li[i+2][j:j+3]
            
            if len(set(li2)) != 9 :
                return 0
    else :
        return 1

for test_case in range(1, T+1):    
    
    li = [list(map(int, input().split())) for _ in range(9)]
    
    ans = solve()

    print(f'#{test_case} {ans}')