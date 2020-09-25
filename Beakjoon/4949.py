while True:
    sen = input()
    if sen == '.':
        break
    
    stack = []
    braek = True
    
    for char in sen:
        if char == '(':
            stack.append(char)
        elif char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(': stack.pop()
            else:
                braek = False
                break
        elif char == ']':
            if stack and stack[-1] == '[': stack.pop()
            else:
                braek = False
                break

    if braek and not stack:
            print('yes')
    else:
        print("no")