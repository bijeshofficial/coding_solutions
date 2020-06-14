def t(n):
    f = 5
    z = 0
    while f<= n:
        z += n//f
        f *= 5
    print(z)
n = int(input())
t(n)