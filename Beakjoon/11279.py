import heapq
import sys
heap = []
n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, -num)
    else:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)