n = int(input())

for i in range(n):
    h, w, n = list(map(int, input().split()))
    o = ((n-1)//h) + 1
    f = ((n-1)%h) + 1
    print(f*100+o)