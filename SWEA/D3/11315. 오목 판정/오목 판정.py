T = int(input())

def solve() :
    for si in range(N) :
        for sj in range(N) :
            for di, dj in ((0,1),(-1,1),(1,1),(1,0)) :
                cnt = 0
                for i in range(5) :
                    ni = si + di *i
                    nj = sj + dj * i
                    if 0 <= ni<N and 0<=nj<N and li[ni][nj] == 'o' :
                        cnt+=1
                    else :
                        break
                if cnt == 5 :
                    return "YES"
    return "NO"

for test_case in range(1, T+1) :
    N=int(input())
    li = [input() for _ in range(N)]
    ans = solve()
    print(f"#{test_case} {ans}")