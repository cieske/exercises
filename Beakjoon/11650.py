n = int(input())
lst = []
for _ in range(n):
    w = list(map(int, input().split()))
    lst.append(w)

lst = sorted(lst, key = lambda x: (x[0], x[1]))

for w in lst:
    print(w[0], w[1])