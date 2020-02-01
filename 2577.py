a = 1
for i in range(3):
    a *= int(input())
b = [int(x) for x in str(a)]
for i in range(10):
    print(b.count(i))