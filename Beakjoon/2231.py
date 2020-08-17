x = int(input())
sol = 0
for i in range(1, x):
    num = list(map(int, str(i)))
    if sum(num) + i == x:
        sol = i
        break

print(sol)