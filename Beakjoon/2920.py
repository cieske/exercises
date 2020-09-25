lst = list(map(int, input().split()))

if lst[0] < lst[1]:
    status = 'ascending'
else:
    status = 'descending'

for i in range(1, len(lst)-1):
    if lst[i] < lst[i+1] and status == 'ascending':
        pass
    elif lst[i] > lst[i+1] and status == 'descending':
        pass
    else:
        status = 'mixed'
        break

print(status)

