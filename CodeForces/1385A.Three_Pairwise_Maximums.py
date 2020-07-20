def func(n):
    for i in range(n):
        l = list(map(int,input().split()))
        l.sort()
        if l[0] <= l[1] and l[1] == l[2]:
            print('YES')
            print(l[0], l[0], l[1])
        else:
            print('NO')
n = int(input())
func(n)