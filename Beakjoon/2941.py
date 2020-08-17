a = str(input())
re = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in re:
    a = a.replace(i, '0')
print(len(a))