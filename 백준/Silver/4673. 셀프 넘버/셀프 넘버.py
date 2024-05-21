li = []
for a in range(1, 10):
    li.append(2*a)
    for b in range(10):
        li.append(11*a+2*b)
        for c in range(10):
            li.append(101*a+11*b+2*c)
            for d in range(10):
                if 1001*a+101*b+11*c+2*d <= 10000 :
                    li.append(1001*a+101*b+11*c+2*d)
not_selfnum = list(set(li))

fullnum = [_ for _ in range(1, 10001)]

for i in fullnum:
    if i not in not_selfnum:
        print(i)