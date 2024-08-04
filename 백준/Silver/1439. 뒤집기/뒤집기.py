S = list(str(input()))
count = 0

for i in range(len(S)-1):
   if S[i] == S[i+1] :
       count = count
   else :
       count += 1
if count == 1 :
    print(count)
elif count % 2 == 0 :
    print(int(count/2))
else :
    print(int((count+1)/2))