def func(n):
    for i in range(n):
        k = int(input())
        l = list(map(int,input().split()))
        odd = 0
        even = 0
        if sum(l)% 2 != 0:
            print('YES')
            continue
        for i in l:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        if even == len(l):
            print('NO')
        elif odd == len(l):
            print('NO')
        else:
            print('YES')
n = int(input())
func(n)