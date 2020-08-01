'''
n = int(input())
lst = list(map(int, input().split()))

sol = [0]*n
max_h = lst[-1]
start = n

for idx in range(n-2, -1, -1):
    if lst[idx] >= max_h:
        max_h = lst[idx]
        sol[idx+1:start] = [idx+1]*(start-(idx+1))
        start = idx+1

for i in range(n):
    print(sol[i], end = ' ')
'''

n = int(input())
lst = list(map(int, input().split()))

stack = []
sol = [0]*n

for idx in range(n-1, -1, -1):
    while stack and lst[stack[-1]] < lst[idx]:
        sol[stack.pop()] = idx+1
    stack.append(idx)
print(*sol)