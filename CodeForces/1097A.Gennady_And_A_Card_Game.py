def func(n):
    h = list(map(str,input().split()))
    num = n[0]
    sign = n[1]
    for i in h:
        if num in i or sign in i:
            print('YES')
            return
    print('NO')
n = input()
func(n)