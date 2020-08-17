x = int(input())
lst = []

for i in range(x):
    num = int(input())
    if num:
        lst.append(num)
        continue
    lst.pop()

print(sum(lst))