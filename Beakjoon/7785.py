import sys 
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(list(map(str, sys.stdin.readline().split())))

log_dict = {}
for log in lst:
    if log[1] == 'enter':
        log_dict[log[0]] = 1
    elif log[1] == 'leave':
        del log_dict[log[0]]

name = sorted(log_dict.keys(), reverse=True)

for na in name:
    print(na)