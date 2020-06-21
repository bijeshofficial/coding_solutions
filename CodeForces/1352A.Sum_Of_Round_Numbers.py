def func(n):
    for i in range(n):
        k = int(input())
        l = []
        i = 1
        while k > 0:
            if k % 10 > 0:
                l.insert(0,(k%10)*i)
            k //= 10
            i *= 10
        print(len(l))
        print(*l)
n = int(input())
func(n)