N, M = map(int, input().split())



# print(weight)

if N == 0 :
    print(0)
else :
    boxes = input().split()

    for i in range(N) :
        boxes[i] = int(boxes[i])

    cnt = 1
    weight = 0
    for box in boxes :
        if weight + box <= M :
            weight += box
        else :
            weight = box
            cnt += 1
    print(cnt)