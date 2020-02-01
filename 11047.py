n, m = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(int(input()))
a = 0
while m != 0:
    a += m//l[n-1]
    m -= l[n-1]*(m//l[n-1])
    n -= 1
print(a)
 
