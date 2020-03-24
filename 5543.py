b = []
d = []

for i in range(5):
    a = int(input())
    if i < 3:
        b.append(a)
    else:
        d.append(a)

print(min(b) + min(d) - 50)