num = int(input())
for i in range(num):
    a, b = list(map(int, input().split()))
    print("Case #%d:"%(i+1), a+b)