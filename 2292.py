import math
n = int(input())

def s(n):
    a = 1
    b = 1
    while n >= a:
        a += b
        b += 1
    return b

print(s(math.ceil((n-1)/6)))