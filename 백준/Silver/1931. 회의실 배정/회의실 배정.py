N = int(input())

li = []
cnt_li = []
for _ in range(N):
    S, E = map(int, input().split())

    li.append([S, E])
# 끝나는 시간을 기준으로 오름차순 정렬
li.sort(key=lambda x:(x[1], x[0]))
# print(li)

for i in range(2):
    cnt = 1
    for k in range(i+1, N):
        if li[i][1] <= li[k][0] :
            cnt += 1
            i = k
        
    cnt_li.append(cnt)
print(max(cnt_li))