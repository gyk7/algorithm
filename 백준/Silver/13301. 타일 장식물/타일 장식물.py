N = int(input())

short_height = 1
long_height = 1 


for i in range(N-1):
    temp = long_height
    long_height = short_height
    short_height = temp
    long_height = short_height + long_height
    # print(f"{short_height}" + "*")
    # print(f"{long_height}" + "^")
    
result = (short_height + long_height) * 2
print(result)