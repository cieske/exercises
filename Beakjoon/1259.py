while True:
    n = int(input())
    if not n:
        break

    n = str(n)
    if len(n)%2 == 0:
        f = n[:len(n)//2]
        b = n[(len(n)//2):][::-1]
    else:
        f = n[:len(n)//2]
        b = n[(len(n)//2)+1:][::-1]
    
    if f == b:
        print('yes')
    else:
        print('no')