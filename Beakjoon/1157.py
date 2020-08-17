a = str(input())
n = []
for i in range(26):
    n.append(a.count(chr(65+i)) + a.count(chr(97+i)))
m = max(n)
if n.count(m) > 1:
    print("?")
else:
    print(chr(n.index(m)+65))