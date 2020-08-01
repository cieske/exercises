import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
poke_lst = []
poke_dic = {}

for i in range(n):
    poke = sys.stdin.readline().rstrip()
    poke_lst.append(poke)
    poke_dic[poke] = i+1

for q in range(m):
    inp = str(sys.stdin.readline().rstrip())
    if inp.isdigit():
        print(poke_lst[int(inp)-1])
    else:
        print(poke_dic[inp])