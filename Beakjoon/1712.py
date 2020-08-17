a, b, c = list(map(int, input().split()))
if c > b:
    print(1 + int(a/(c-b)))
else:
    print(-1)