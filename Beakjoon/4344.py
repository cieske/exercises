n = int(input())
for i in range(n):
    s = list(map(int, input().split()))[1:]
    h = [x for x in s if x > sum(s)/len(s)]
    print("%.3f%%"%(len(h)*100/len(s)))    
