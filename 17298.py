n = int(input())
lst = list(map(int, input().split()))

stack = []
sol = [-1]*n

for idx in range(n):
    while stack and lst[stack[-1]] < lst[idx]:
        sol[stack.pop()] = idx
    stack.append(idx)

sol = [lst[x] if x != -1 else -1 for x in sol]
print(*sol)