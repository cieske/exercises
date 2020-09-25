import sys

n =  int(input())
que = []

for _ in range(n):
    com = sys.stdin.readline().split()
    
    if com[0] == 'push':
        que.append(int(com[1]))

    elif com[0] == 'pop':
        if que: print(que.pop(0))
        else: print(-1)

    elif com[0] == 'size':
        print(len(que))

    elif com[0] == 'empty':
        if que: print(0)
        else: print(1)

    elif com[0] == 'front':
        if que: print(que[0])
        else: print(-1)

    elif com[0] == 'back':
        if que: print(que[-1])
        else: print(-1)