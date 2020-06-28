def func(n):
    for i in range(n):
        l = list(map(int,input().split()))
        counter = l[-1]
        a = l[0]
        b = l[1]
        c = l[2]
        x = max(a,b,c)
        # flag = True
        # while a != x or b != x or c != x:
        counter -= x - a
        counter -= x - b
        counter -= x - c
        if counter%3 != 0 or counter < 0:
            print('NO')
        else:
            print('YES')
            
n = int(input())
func(n)