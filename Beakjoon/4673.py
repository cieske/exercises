def d(n):
    return n + sum([int(i) for i in str(n)])

s = set(range(1, 10001))
for i in range(1, 10001):
    if d(i) in s:
        s.remove(d(i))

for i in s:
    print(i)