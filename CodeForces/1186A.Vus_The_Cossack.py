def func(n):
    if n[1] < n[0] or n[2] < n[0]:
        print('NO')
    else:
        print('YES')
n = list(map(int,input().split()))
func(n)