def hansoo(n):
    s = str(n)
    cha = int(s[0]) - int(s[1])
    for i in range(len(s)-2):
        if int(s[i+1]) - int(s[i+2]) != cha:
            return 0
    return 1

n = int(input())
if n < 100:
    print(n)
else:
    y = []
    for i in range(100, n+1):
        y.append(hansoo(i))
    num = y.count(1)
    print(99+num)