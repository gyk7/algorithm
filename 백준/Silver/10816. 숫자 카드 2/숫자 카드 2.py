from collections import Counter
N = int(input())
K = list(map(int, input().split()))
M = int(input())
q = list(map(int, input().split()))

hash_map = {}
# print(list(K))
# print(list(q))
counter = Counter(K)
for i in set(K):  
    hash_map[i] = counter[i]

# print(hash_map)
find_map = dict(zip(range(len(q)),q))
# print(find_map)

for k, v in find_map.items() :
    print(hash_map.get(v, 0), end =' ')