import sys
input=sys.stdin.readline

x = int(input())
lst = []
for i in range(x):
    op = list(map(str, input().split()))
    if op[0] == 'push':
        lst.append(op[1])
    elif op[0] == 'pop':
        if lst:
            print(lst[-1])
            lst.pop()
        else:
            print(-1)
    elif op[0] == 'size':
        print(len(lst))
    elif op[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    elif op[0] == 'top':
        if lst:
            print(lst[-1])
        else:
            print(-1)