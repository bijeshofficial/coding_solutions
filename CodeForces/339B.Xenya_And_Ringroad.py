def func(n):
    k = list(map(int,input().split()))
    current = 1
    count = 0
    for i in range(n[1]):
        if k[i] > current:
            count += k[i] - current
            current = k[i]
        elif k[i] < current:
            count += n[0]-current
            current = 0
            count += k[i]-current
            current = k[i]
    print(count)
n = list(map(int,input().split()))
func(n)