lst = list(map(int, input().split()))
mul = [x**2 for x in lst]
print(sum(mul)%10)