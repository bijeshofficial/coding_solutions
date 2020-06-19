def func(n):
    for i in range(n):
        k = int(input())
        if k % 2 == 0:
            print(k//2 -1)
        else:
            print(k//2)
n = int(input())
func(n)