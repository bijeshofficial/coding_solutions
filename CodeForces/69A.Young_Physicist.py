n = int(input())
x = 0
y = 0
z = 0
for i in range(n):
    k = list(map(int,input().split()))
    x += k[0]
    y += k[1]
    z += k[2]
if x == 0 and y == 0 and z == 0:
    print('YES')
else:
    print('NO')