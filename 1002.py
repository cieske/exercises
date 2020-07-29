n = int(input())
for i in range(n):
    a, b, c, x, y, z = map(int, input().split())

    d = ((a-x)**2 + (b-y)**2)**0.5
    r = c-z
    s = c+z

    if d == 0 and c == z:
        print(-1)
    elif d > s:
        print(0)
    elif d == s or c+d == z or d+z == c:
        print(1)
    elif d+c<z or d+z<c:
        print(0)
    else:
        print(2)