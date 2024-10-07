from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin, words, target, 0)

def bfs(begin, words, target, step) :
    q = deque()
    q.append((begin, 0))
    
    while q :
        now, step = q.popleft()
        
        if now == target :
            return step
        
        
        for word in words :
            cnt = 0
            for i in range(len(word)):
                if word[i] != now[i] :
                    cnt += 1
                    
            if cnt == 1 :
                q.append((word, step + 1))