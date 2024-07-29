word = input()
li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for i in li :
    word = word.replace(i, '*')
print(len(word))