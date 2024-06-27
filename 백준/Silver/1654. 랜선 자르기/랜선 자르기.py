K, N = map(int, input().split())
li = []
for i in range(K) :
    length = input()
    li.append(int(length))
    
li.sort()

start = 1
end = max(li)

    
while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in li :
        sum += i // mid
        # print(sum)
    if sum < N :
        end = mid - 1
    else :
        start = mid + 1
print(end)