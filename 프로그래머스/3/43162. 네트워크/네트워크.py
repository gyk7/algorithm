def solution(n, computers) :
    def dfs(row, computers) :
        for j in range(n):
            if computers[row][j] == 1 :
                computers[row][j] = 0
                computers[j][row] = 0
                dfs(j, computers)    
                
    answer = 0
    for r in range(len(computers)):
        if computers[r][r] == 1:
            dfs(r, computers)
            answer += 1 
    return answer
