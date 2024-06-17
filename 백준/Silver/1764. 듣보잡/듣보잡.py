from collections import Counter
N, M = map(int, input().split())
hash_map = {}
li = []

for _ in range(N+M):
    name = input()
    li.append(name)

hash_map=Counter(li)

print(N+M - len(hash_map))
hash_map = dict(sorted(hash_map.items()))
# print(hash_map)

for k, v in hash_map.items() :
    if v == 2 :
        print(k)