N = int(input())
room = []

for i in range(N) :
    room.append(input())
# print(room)

width = 0
for i in range(N) :
    space = 0
    for j in range(N) :
        if room[i][j] == '.':
            space += 1
            if space == 2 :
                width += 1
        else :
            space = 0
            continue

height = 0
for i in range(N) :
    space = 0
    for j in range(N) :
        if room[j][i] == '.' :
            space += 1
            if space == 2 :
                height += 1
        else :
            space = 0
            continue

print(width, height)