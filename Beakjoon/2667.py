import sys

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n or lst[x][y] == '0':
        return 0#시작점이 0이면 바로 종료
    
    #지점에 아파트가 있는 경우
    stack = []
    lst[x][y] = '0' #이미 지나온 곳 0으로 초기화
    count = 1
    stack.append([x,y])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while stack: #스택이 차 있는 동안
        loc = stack.pop()
        for i in range(4):
            new_x = loc[0]+dx[i]
            new_y = loc[1]+dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and lst[new_x][new_y] == '1':
                stack.append([new_x, new_y]) #스택에 집 추가
                count += 1 #집 개수 + 1
                lst[new_x][new_y] = '0' #이미 지나온 곳 0으로 초기화

    return count

n = int(sys.stdin.readline())
lst = [list(sys.stdin.readline()) for _ in range(n)]
sol = []

for r in range(n):
    for c in range(n):
        num_apt = dfs(r, c) #모든 지점에 대해 수행
        if num_apt:
            sol.append(num_apt)

sol.sort()
print(len(sol))
for j in range(len(sol)):
    print(sol[j])