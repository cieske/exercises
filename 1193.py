n = int(input())

# def s(n):
#     a = 1
#     b = 1
#     while n >= a:
#         a += b
#         b += 1
#     return a, b
# a, b = s(n)
# x, y = b-(a-n), (a-n)

def s(n):
    a = 1
    b = 1
    while n >= a:
        a += b
        b += 1
    return b-(a-n), a-n, b
x, y, b = s(n)

if b%2==1:
    print("%d/%d"%(x, y))
else:
    print("%d/%d"%(y, x))