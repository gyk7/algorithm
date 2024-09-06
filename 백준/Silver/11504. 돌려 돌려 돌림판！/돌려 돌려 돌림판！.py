T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    X = input().split()
    Y = input().split()
    X = ''.join(X)
    X = int(X)
    Y = ''.join(Y)
    Y = int(Y)
    li = list(map(int, input().split()))
    # print(type(X))
    # print(li)
    li += li[:M]
    res = 0
    
    for i in range(N):
        check = int(''.join(map(str, li[i:i+M])))
        if X <= check <= Y :
            res += 1
    
    print(res)