def func(n):
    for i in range(n):
        k = list(map(int,input().split()))
        a = k[0]
        b = k[1]
        if (a+b) % 3 ==0 and 2*a >=b and 2*b >= a:
            print('YES')
        else:
            print('NO')
n = int(input())
func(n)