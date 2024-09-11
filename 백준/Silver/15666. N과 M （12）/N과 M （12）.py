N, M = map(int, input().split())

li = list(map(int, input().split()))
li.sort()

ans = [0]*M
def back(k, idx) :
    if k == M:
        for i in range(M):
            print(ans[i], end=' ')
        print()
        return

    temp = 0
    for i in range(idx, N):
        if temp != li[i]:
            ans[k] = li[i]
            temp = li[i]
            back(k+1, i)

back(0, 0)