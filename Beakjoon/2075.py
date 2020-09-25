import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split())) #초기 N개 수

for _ in range(n-1): #N개씩 수가 들어올때마다
    tmp_lst = sorted(list(map(int, sys.stdin.readline().split())) + lst) #합치고 정렬
    lst = tmp_lst[n:] #가장 큰 N개만 빼서 저장

print(lst[0])