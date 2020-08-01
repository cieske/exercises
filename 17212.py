n = int(input())
dp = [100001]*(n+1)
dp[0] = 0
coin = [7, 5, 2, 1]

for m in range(1, n+1):
    for c in coin:
        if c <= m and dp[m-c]+1 < dp[m]:
            dp[m] = dp[m-c]+1
print(dp[-1])