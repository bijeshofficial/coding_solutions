def func(n):
    counter = 0
    for i in range(1,n[0]+1):
        if n[1] % i == 0:
            if n[1] <= (i*n[0]):
                counter += 1
    print(counter)
n = list(map(int,input().split()))
func(n)