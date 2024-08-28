import sys
input = sys.stdin.readline
M = int(input())
S = set()
for _ in range(M):
    K = input()
    K = K.split()
    # print(comment)
    comment = K[0]
    # print(comment)
    if comment == 'add' :
        S.add(K[1])
    elif comment == 'check' :
        if K[1] in S :
            print(1)
        else :
            print(0)
    elif comment == 'remove' :
        if K[1] in S :
            S.remove(K[1])
    elif comment == 'toggle' :
        if K[1] in S :
            S.remove(K[1])
        else :
            S.add(K[1])
    elif comment == 'empty' :
        S = set()
    elif comment == 'all' :
        S = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])