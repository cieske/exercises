lst = []
for i in range(5):
    a = int(input())
    lst.append(a)

lst = [40 if x <= 40 else x for x  in lst]

print(sum(lst)//5)