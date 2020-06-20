def func(n):
    n1 = n//2
    n2 = n - n1
    while n1 % 2 != 0 or n2 % 3 != 0:
        n1 -= 1
        n2 += 1
    print(f'{n1} {n2}')
n = int(input())
func(n)