from collections import deque

def bfs(x, y):
    if farm[y][x] == 0:
        return 0
    q = deque()
    q.append([x,y])
    while q:
        a, b = q.popleft()
        for f in range(4):
            new_y = b + dy[f]
            new_x = a + dx[f]
            if 0 <= new_y < n and 0 <= new_x < m and farm[new_y][new_x] == 1:
                farm[new_y][new_x] = 0
                q.append([new_x, new_y])
    return 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())

for _ in range(n):
    ans = 0
    m, n, k = map(int, input().split())
    farm = [[0]*m for x in range(n)] #밭 초기화
    for __ in range(k):
        a, b = map(int, input().split())
        farm[b][a] = 1 #배추 위치 초기화

    for i in range(m):
        for j in range(n):
            s = bfs(i,j)
            if s:
                ans += 1
    print(ans)