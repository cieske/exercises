n, e, s = list(map(int, input().split()))
e_list = []
for i in range(e):
    n1, n2 = list(map(int, input().split()))
    e_list.append([n1, n2])

#DFS
stack = [s]
result = [s]
while stack:
    cur = stack[-1]
    cur_nei = []
    for pair in e_list:
        if cur == pair[0]:
            cur_nei.append(pair[1])
        elif cur == pair[1]:
            cur_nei.append(pair[0])
    cur_nei = sorted(cur_nei)

    exit = True
    for i in cur_nei:
        if i not in result:
            stack.append(i)
            result.append(i)
            exit = False
            break
    if exit:
        stack.pop()
print(result)

# #BFS
# queue = [s]
# result = []
# while queue:
#     cur = queue[0]
#     cur_nei = []
#     for pair in e_list:
#         if cur == pair[0]:
#             cur_nei.append(pair[1])
#         elif cur == pair[1]:
#             cur_nei.append(pair[0])

#     for i in cur_nei:
#         if i not in queue:
#             queue.append(i)
#     result.append(queue.pop(0))

# print(result)
        

