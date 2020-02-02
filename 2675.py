n = int(input())
for i in range(n):
    a, b = list(map(str, input().split()))
    for j in b:
        for k in range(int(a)):
            print(j, end = '')
    print()