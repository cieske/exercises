n = int(input())
stack = []

for i in range(n):
    early = True
    stack = []
    x = str(input())
    for s in x:
        if s == '(':
            stack.append(1)
        if s == ')':
            if len(stack) == 0:
                print("NO")
                early = False
                break
            else:
                stack.pop()
    if early:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")