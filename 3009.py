a,b = list(map(int, input().split()))
c,d = list(map(int, input().split()))
e,f = list(map(int, input().split()))

if a==c:
    x = e
elif a==e:
    x = c
else:
    x = a

if b==d:
    y = f
elif b==f:
    y = d
else:
    y = b

print(x, y)