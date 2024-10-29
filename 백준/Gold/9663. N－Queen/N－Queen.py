def dfs(n) :
    global ans
    # 종료 조건 처리 + 정답 처리
    if n == N : #  N행까지 진행한 경우 경우의 수 가능 : 성공
        ans += 1    # 경우의 수 + 1    
        return 
    
    for j in range(N) :
        if v1[j] == 0 and v2[n+j] == 0 and v3[n-j] == 0 : # 열, 대각선 모두 없는 경우
            v1[j] = 1
            v2[n+j] = 1
            v3[n-j] = 1
            dfs(n+1)
            v1[j] = 0
            v2[n+j] = 0
            v3[n-j] = 0


N = int(input())

ans = 0
v1 = [0] * (N+1)    # 중복 확인을 위한 visited[] 열
v2 = [0] * (2*N)    # 중복 확인을 위한 visited[] 오른쪽 대각선
v3 = [0] * (2*N)    # 중복 확인을 위한 visited[] 왼쪽 대각선
dfs(0)
print(ans)
    