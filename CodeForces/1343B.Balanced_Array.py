def func(n):
    for i in range(n):
        y = int(input())
        even = [x for x in range(1,y+1) if x%2 == 0 ]
        odd = [x for x in range(1,y+1) if x%2 != 0 ]
        odd[-1] += y//2
        if y % 4 != 0:
            print('NO')
        else:
            print('YES')
            print(*even+odd)
n = int(input())
func(n)