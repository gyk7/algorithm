T = int(input())
stack = []
for i in range(T):
    k = input()
    stack.append(list(k))

    
for j in range(T):
    stack2 = []
    for _ in range(len(stack[j])):
        
        top = stack[j].pop()
               
        if top == ')':
            stack2.append(')')
        elif top == '(':
            if ')' in stack2 :
                stack2.remove(')')
            else :
                stack2.append('(')
        # print(stack2)
    if stack2 == [] :
        print("YES")
    else:
        print("NO")