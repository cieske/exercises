from sys import stdin

n = int(input())
lst = []

for _ in range(n):
    lst.append(stdin.readline().split())
lst = sorted(lst, key = lambda x: int(x[0])) 

for c in lst:
    print(*c)