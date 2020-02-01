while True:
    a, b = list(map(int, input().split()))
    if a==b:
        break
    elif a%b == 0:
        print("multiple")
    elif b%a == 0:
        print("factor")
    else:
        print("neither")