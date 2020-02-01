a, num, i = int(input()), -1, 0
b = a
while num != b:
    num = (a%10+a//10)%10 + (a%10)*10
    a = num
    i += 1
print(i)
