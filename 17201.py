n = int(input())
mag = input()
ds = True
for i in range(2*n-1):
    print(mag[i], mag[i+1])
    if mag[i] == mag[i+1]:
        ds = False
        break
if ds:
    print("Yes")
else:
    print("No")    