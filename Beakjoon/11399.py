n = int(input())
a = list(map(int, input().split()))
a.sort()
b = 0
for i in range(1, n):
    a[i] += a[i-1]
print(sum(a))