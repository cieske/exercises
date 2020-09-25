def dfs():
    visited = [False]*(n+1)
    con = [1]
    while con:
        cur = con.pop()

        if not visited[cur]:
            visited[cur] = True
            if cur in dic:
                con += dic[cur]
    return sum(visited)

n = int(input())
m = int(input())
dic = dict()

for _ in range(m):
    a, b = map(int, input().split())

    if a not in dic:
        dic[a] = [b]
    else:
        dic[a].append(b)
    if b not in dic:
        dic[b] = [a]
    else:
        dic[b].append(a)

x = dfs()
print(x-1)