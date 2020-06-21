def func(k):
    n = k[0]
    m = k[1]
    counter = n
    i = 1
    while i*m <= n:
        counter += 1
        i += 1
        n += 1
    print(counter)
k = list(map(int,input().split()))
func(k)