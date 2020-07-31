def func(t):
    for i in range(t):
        n = list(map(int,input().split()))
        a = list(map(int,input().split()))
        x = n[1]
        odd = 0
        for i in a:
            if i % 2 != 0:
                odd += 1
        if odd == 0:
            print('NO')
            continue
        elif odd == n[0] and x %2 == 0:
            print('NO')
            continue
        elif x == n[0] and odd % 2 ==0:
            print('NO')
            continue
        print('YES')
t = int(input())
func(t)