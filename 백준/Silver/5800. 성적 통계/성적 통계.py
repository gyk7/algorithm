K = int(input())
for i in range(K):
    Class = list(map(int, input().split()))
    score = Class[1:]
    score.sort(reverse=True)
    gap_li = []
    for j in range(len(score)-1):
        gap = score[j] - score[j+1]
        gap_li.append(gap)
        Largest_Gap = max(gap_li)
        
    print("Class " + f"{i+1}")
    print("Max " + f"{score[0]}" + "," + " Min " + f"{score[-1]}" + "," + " Largest gap " + f"{Largest_Gap}" )