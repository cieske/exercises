n = int(input())
for i in range(n):
    a = list(map(str, input()))
    s, t = 0, 0
    for j in a:
        if j == 'O':
            t += 1
            s += t
        else:
            t = 0
    print(s)