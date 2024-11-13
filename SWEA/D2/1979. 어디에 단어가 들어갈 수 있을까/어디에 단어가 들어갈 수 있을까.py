T = int(input())

def find(arr, length):
    cnt = 0
    for li in arr:
        for i in range(len(li)-length+1):
            if sum(li[i:i+length]) == length :
                if i == 0 :
                    if li[i+length] == 0 :
                        cnt += 1
                elif i == len(li)-length :
                    if li[i-1] == 0 :
                        cnt += 1
                else :
                    if li[i-1] == 0 and li[i+length] == 0 :
                        cnt +=1  
    return cnt    

for test_case in range(1, T+1) :
    result = 0
    N, K = map(int, input().split())
    arr1=[list(map(int, input().split())) for _ in range(N)]
    arr2=[list(x) for x in zip(*arr1)]
    
    result = find(arr1, K) + find(arr2, K)
    
    print(f"#{test_case} {result}")
    