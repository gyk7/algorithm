while True :
    N = int(input())
    start = 1
    end = 50
    
    if N == 0 :
        break
    while True :
        k = (start + end) // 2
        print(k, end=' ')
        if N == k:
            break
    
        elif N > k :
            start = k + 1
        
        else :
            end = k - 1
    print("")