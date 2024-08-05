N, M = map(int, input().split())

li = []

A = list(map(int, input().split()))
# print(A)

B = list(map(int, input().split()))
# print(B)

li = A + B
li.sort()
print(*li)