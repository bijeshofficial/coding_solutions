def func(n):
    for i in range(n):
        k = list(map(int,input().split()))
        h = k[0]
        n1 = k[1]
        m = k[2]
        if h <= m*10:
            print('YES')
            continue
        while n1 > 0:
            h = (h//2) + 10
            n1 -= 1
            # print(h)
        while m > 0:
            h -= 10
            m -= 1
            # print(h)
        if h <= 0:
            print('YES')
        else:
            print('NO')
n = int(input())
func(n)