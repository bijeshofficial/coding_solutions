def func(n):
    counter = 0
    for i in range(n):
        l = list(map(int,input().split()))
        p1 = l[0]
        q1 = l[1]
        if p1 < q1:
            counter += 1
    if counter > 0:
        print('Happy Alex')
    else:
        print('Poor Alex')
n = int(input())
func(n)