import sys

n =  int(input())
deque = []

for _ in range(n):
    com = sys.stdin.readline().split()

    if com[0] == 'push_front':
        deque = [com[1]] + deque

    elif com[0] == 'push_back':
        deque.append(com[1])

    elif com[0] == 'pop_front':
        if deque: print(deque.pop(0))
        else: print(-1)
    
    elif com[0] == 'pop_back':
        if deque: print(deque.pop())
        else: print(-1)
    
    elif com[0] == 'size':
        print(len(deque))
    
    elif com[0] == 'empty':
        if deque: print(0)
        else: print(1)

    elif com[0] == 'front':
        if deque: print(deque[0])
        else: print(-1)

    elif com[0] == 'back':
        if deque: print(deque[-1])
        else: print(-1)