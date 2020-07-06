def func(a):
    n = a[0]
    k = a[1]
    l = a[2]
    c = a[3]
    d = a[4]
    p = a[5]
    nl = a[6]
    np = a[7]
    x = (k * l) // nl
    y = c * d
    z = p // np
    print(min(x,y,z)//n)
a = list(map(int,input().split()))
func(a)