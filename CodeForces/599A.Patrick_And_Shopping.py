def func(a):
    x = a[0] + a[2] + a[1]
    y = a[0] + a[2] + a[2] + a[0]
    w = a[1] + a[1] + a[0] + a[0]
    z = a[1] + a[2] + a[2] + a[1]
    print(min(x,y,z,w))
a = list(map(int,input().split()))
func(a)