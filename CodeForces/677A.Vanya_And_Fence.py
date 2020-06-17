def func(n):
    x = list(map(int,input().split()))
    h = n[1]
    counter = 0
    for i in x:
        if i <= h:
            counter += 1
        else:
            counter += 2
    print(counter)
n = list(map(int,input().split()))
func(n)