n = int(input())

people = {}
li = []

for i in range(n):
    name, state = input().split()
    people[name] = state
# print(people)    
for name in people.keys() :
    if people[name] == 'enter':
        li.append(name)
li.sort(reverse=True)
print(*li)