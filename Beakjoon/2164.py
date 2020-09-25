a = int(input())
lst = list(range(1, a+1))

while len(lst) > 1:
    if len(lst)%2 == 0:
        lst = lst[1::2]
    else:
        lst = [lst[-1]] + lst[1::2]
print(*lst)


# n, m = int(input()), 1

# while n>m:
#     m*=2
# print(n*2-m)