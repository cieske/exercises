a, b = list(map(str, input().split()))
a, b = int(a[::-1]), int(b[::-1])
print(max(a, b))
