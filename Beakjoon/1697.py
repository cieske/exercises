n = int(input())
price = list(map(int, input().split()))
sol = [price[0]] + [0]*(n-1)

for i in range(1, len(sol)):    
    #예를 들어 i=3이면, 3장짜리 팩을 살 수도 있고, 2장까지의 최고가에 1장짜리 팩을 살 수도 있고
    #1장까지의 최고가에 2장짜리 팩을 살 수도 있다.
    sol[i] = max([(sol[j]+price[i-j-1]) for j in range(i)]+[price[i]])
print(sol[-1])