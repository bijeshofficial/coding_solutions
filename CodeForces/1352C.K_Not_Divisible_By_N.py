def func(l):
    for i in range(l):
        b = list(map(int,input().split()))
        n = b[0]
        k = b[1]
        a = (k - 1) // (n - 1)
        print(k + a)
l = int(input())
func(l)