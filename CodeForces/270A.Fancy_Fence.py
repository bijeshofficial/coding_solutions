n = int(input())
for i in range(n):
    angle = int(input())
    ans1 = 360/(180-angle)
    ans2 = 360//(180-angle)
    if ans1 == ans2:
        print('YES')
    else:
        print('NO')