a, b, c, n = map(int, input().split())

lst = [0]*301
lst[a] = 1
lst[b] = 1
lst[c] = 1

for i in range(1, n+1):
    if lst[i] or lst[i-a] or lst[i-b] or lst[i-c]:
        lst[i] = 1
    else:
        lst[i] = 0
print(lst[n])

#출처 : https://docp.tistory.com/