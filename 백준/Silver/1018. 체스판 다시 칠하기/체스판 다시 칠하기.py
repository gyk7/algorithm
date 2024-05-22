N, M = map(int, input().split())
board=[]
result=[]

for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        draw1 = 0
        draw2 = 0

        for p in range(i,i+8):
            for q in range(j,j+8):
                if (p+q) % 2 == 0 :
                    if board[p][q] != 'B':
                        draw1+=1
                    else :
                        draw2+=1
                else:
                    if board[p][q] != 'W':
                        draw1+=1
                    else :
                        draw2+=1

        result.append(draw1)
        result.append(draw2)

print(min(result))