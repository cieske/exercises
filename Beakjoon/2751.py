from sys import stdin

n = int(stdin.readline())
lst = []
for _ in range(n):
    lst.append(int(stdin.readline().replace('\n', '')))

lst = sorted(lst)
print(*lst, sep="\n")