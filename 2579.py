n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

if n > 3:
    dp = [lst[0], max(lst[0]+lst[1], lst[1]), max(lst[0]+lst[2], lst[1]+lst[2])]
    for i in range(3, len(lst)):
        dp.append(max(dp[i-2]+lst[i], dp[i-3]+lst[i-1]+lst[i]))
    print(dp[-1])
else:
    print(sum(lst))