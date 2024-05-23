N = int(input())

bag_n = 0

bag_n = N // 5

if N % 5 % 3 == 0 :
    bag_n += N % 5 // 3
elif bag_n == 0 or N == 7 :
    bag_n = -1
else :
    while bag_n > 0 :
        bag_n -= 1
        
        if (N - bag_n * 5) % 3 == 0:
            bag_n += (N - bag_n * 5)//3
            break
print(bag_n)