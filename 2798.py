n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
q = m
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            s = l[i]+l[j]+l[k]
            if m-s>=0:
                q = min(q, m-s)
print(m-q)