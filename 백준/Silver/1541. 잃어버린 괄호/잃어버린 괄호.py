result = 0
formula = input().split('-')


#print(formula)
for i in range(len(formula)) :
    if "+" in formula[i] :
        sum = 0
        N = formula[i].split("+")
        for k in N :
            sum+=int(k)
        formula[i] = sum
    else :
        formula[i] = int(formula[i])
#print(formula)
result+=formula[0]
for p in range(1, len(formula)):
    result-=formula[p]
print(result)