# 딕셔너리 쓰니까 시간 초과 => 아마 sorting?
# from sys import stdin

# n = int(stdin.readline())
# dic = dict()

# for _ in range(n):
#     m = int(stdin.readline())
#     if m in dic:
#         dic[m] += 1
#     else:
#         dic[m] = 1

# for pair in sorted(dic.items()):
#     for iter in range(pair[1]):
#         print(pair[0])

#리스트 쓰니까 통과
from sys import stdin

n = int(stdin.readline())
lst = [0]*10001

for _ in range(n):
    lst[int(stdin.readline())] += 1

for idx, val in enumerate(lst):
    if val != 0:
        for _ in range(val):
            print(idx)