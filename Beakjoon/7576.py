from collections import deque

m, n = map(int, input().split())
tom = []
queue = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
tmp = m*n #초기 0 개수(익어야 하는 토마토 수)
day = -1
rip = 0 #익은 토마토 수

def bfs():
    global rip
    x, y = queue.popleft()
    for i in range(4): #상하좌우 탐색
        new_x = x+dx[i]
        new_y = y+dy[i]
        if  0 <= new_x < n and 0 <= new_y < m and tom[new_x][new_y] == 0:
            tom[new_x][new_y] = 1 #안 익은 주위의 토마토 1로 변경
            rip += 1 #익은 개수 update
            queue.append([new_x, new_y])


for _ in range(n):
    tom.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if tom[i][j] == 1: #초기에 익은 토마토를 queue에 추가
            queue.append([i,j])
            tmp -= 1
        elif tom[i][j] == -1: #빈 공간 체크
            tmp -= 1


if tmp == 0: #초기에 모두 다 익어있다
    print(0)
else:
    while queue:
        num = len(queue)
        for _ in range(num):
            bfs()
        day += 1

    if tmp == rip: #모두 익는게 가능하다
        print(day)
    else: #모두 익는게 불가능하다
        print(-1)