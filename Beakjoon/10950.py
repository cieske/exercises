num = int(input())
lst = []
for i in range(num):
    lst.append(list(map(int,input().split())))
for i in range(num):
    print(sum(lst[i]))