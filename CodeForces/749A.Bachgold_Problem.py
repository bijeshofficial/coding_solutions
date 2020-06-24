def func(n):
    l = []
    while n > 0:
        if n == 3:
            n = 0
            l.append(3)
        else:
            n -= 2
            l.append(2)
    print(len(l))
    print(*l)
n = int(input())
func(n)