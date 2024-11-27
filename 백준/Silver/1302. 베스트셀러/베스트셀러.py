N = int(input())
sell = {}
for _ in range(N) :
    title = input()
    if title not in sell :
        sell[title] = 1
    else :
        sell[title] += 1

max_value = max(sell.values())

best = []
for k, v in sell.items() :
    if v == max_value :
        best.append(k)

best = sorted(best)
print(best[0])