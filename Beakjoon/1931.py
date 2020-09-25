n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

lst = sorted(lst, key = lambda x :(x[1], x[0]))
print(lst)

count = 0
end_time = 0
for idx in range(n):
    if end_time <= lst[idx][0]:
        count += 1
        end_time = lst[idx][1]

print(count)