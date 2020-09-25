from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
que = deque(range(1, n+1))

print("<", end="")
while que:
    for _ in range(k-1): #k-1번째까지는 살려둠
        que.append(que.popleft())
    print(que.popleft(), end="") #k번째 원소를 뺌
    if que:
        print(", ", end="")
print(">")

#다음 문제는 이 코드로 해결 가능
#11866번 - 요세푸스 문제 0
#1158번 - 요세푸스 문제