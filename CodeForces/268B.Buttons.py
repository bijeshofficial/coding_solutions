def func(n):
    s = 0
    for i in range(0,n):
        s += (n-i)*i
    print(s+n)
n = int(input())
func(n)