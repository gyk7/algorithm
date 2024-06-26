N, M = map(int, input().split())

height = list(map(int, input().split()))

height.sort()

low = 0
high = height[N-1]


while True:
    sum = 0
    mid = (high+low) // 2
    for h in height :
        if h > mid :
            sum += h - mid
    if sum == M or low > high :
        break
        
    elif sum < M :
        high = mid - 1

    else :
        low = mid + 1
    
print(mid)