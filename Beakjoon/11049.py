import sys

n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)] #2차원 배열 생성

for i in range(1, n): #i번째 대각선
    for j in range(n-i): #i번째 대각선의 j번째 열
        dp[j][j+i] = 2**31
        for k in range(j, j+i): #이전 단계 부분문제를 이용해 현재 문제를 푸는 k가지 방법 비교
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + lst[j][0]*lst[k][1]*lst[j+i][1])

print(dp[0][n-1])