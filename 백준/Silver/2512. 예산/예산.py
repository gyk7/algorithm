n = int(input())
li = list(map(int, input().split()))
m = int(input())

li.sort()

start = 1
end = max(li)

while start <= end :
    mid = (start + end) // 2
    sum = 0
    for i in li :
        if i > mid :
            sum += mid 
        else :
            sum += i
    if sum <= m :
        result = mid
        start = mid + 1
    else :
        end = mid - 1
        
print(result)