n = int(input())
pic = []
for _ in range(n): #적록색약이 아닌 사람이 보는 그림(input 그대로)
    pic.append(str(input()))

pic_weak = []
for row in pic: #적록색약인 사람이 보는 그림
    tmp = ['R' if c=='G' else c for c in row]
    pic_weak.append(''.join(tmp))
    

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y, pict):
    stack = [[x,y]]
    color = pict[y][x]
    pict[y] = pict[y][:x] + 'X' + pict[y][x+1:]

    while stack:
        a, b = stack.pop()
        for idx in range(4):
            new_x = a + dx[idx]
            new_y = b + dy[idx]
            if 0 <= new_x < n and 0 <= new_y < n and pict[new_y][new_x] == color:
                stack.append([new_x, new_y])
                pict[new_y] = pict[new_y][:new_x] + 'X' + pict[new_y][new_x+1:]

non_weak = 0
for i in range(n): #적록색약이 아닌 경우에 대해 dfs
    for j in range(n):
        if pic[j][i] != 'X':
            dfs(i,j, pic)
            non_weak += 1
weak = 0
for i in range(n): #적록색약일 경우에 대해 dfs
    for j in range(n):
        if pic_weak[j][i] != 'X':
            dfs(i,j, pic_weak)
            weak += 1

print(non_weak, weak)