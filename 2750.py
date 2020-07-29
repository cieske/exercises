n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst = sorted(lst)
for i in lst:
    print(i)