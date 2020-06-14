n = list(map(int,input().split()))
x = n[0] // n[2]
y = n[1] // n[2]
if n[0] % n[2] != 0:
    x += 1
if n[1] % n[2] !=0:
    y += 1
print(x*y)   