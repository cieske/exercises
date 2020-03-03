n = int(input())
x = []
for i in range(n):
    s = str(input())
    d = True
    while len(s) != 0:
        num = s.count(s[0])
        if s[:num].count(s[0]) != num:
            d = False
            break
        s = s[num:]
    if d:
        x.append(1)
print(x)
print(x.count(1))