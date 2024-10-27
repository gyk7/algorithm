def bfs(f, s, g, u, d) :
    q = []
    q.append(s) # 현재 층 삽입
    v[s] = 1
    
    while q :
        i = q.pop(0) # 현재층 i에 넣기
        
        if i == g :
            return v[i] - 1
        
        for n in (u, -d) : # 업다운할거야
            c = i + n # 현재층에서 업 다운 시행 c : 이동 후 층
            if 0 < c <= f and v[c] == 0 :
                q.append(c)
                v[c] = v[i] + 1
                # v[c] = 0
                # print("##################")
                # print(c)
                # print(v)
        
    return "use the stairs"


F, S, G, U, D = map(int, input().split())
v = [0] * (F+1)
print(bfs(F, S, G, U, D))

#    F : 전체 층
#    S : 현재 층
#    G : 도착 층
#    U : 올라가는 층
#    D : 내려가는 층
#    