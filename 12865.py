n, w = map(int, input().split())
obj = []
for i in range(n):
    obj.append(list(map(int, input().split())))

dp = [[0]*(w+1) for _ in range(n+1)]

for num in range(1, n+1):
    for weight in range(1, w+1):
        if obj[num-1][0] > weight:
            dp[num][weight] = dp[num-1][weight]
        else:
            dp[num][weight] = max(dp[num-1][weight], dp[num-1][weight-obj[num-1][0]]+obj[num-1][1])

print(dp[n][w])