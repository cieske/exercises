import string
L = list(string.ascii_lowercase)
a = input()
for i in L:
    if i in a:
        print(a.index(i), end = ' ')
    else:
        print(-1, end = ' ')