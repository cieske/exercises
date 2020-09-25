n = int(input())
lst = []
for _ in range(n):
    c = str(input())
    lst.append(c)

lst = list(set(lst))

for idx, c in enumerate(lst):
    lst[idx] = [c, len(c)]

lst = sorted(lst, key = lambda x : (x[1], x[0]))

for c in lst:
    print(c[0])