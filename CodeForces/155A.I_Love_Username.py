def func(n):
    k = list(map(int,input().split()))
    first_max = k[0]
    first_less = k[0]
    counter = 0
    for i in range(1,len(k)):
        if k[i] < first_less:
            counter += 1
            first_less = k[i]
        elif k[i] > first_max:
            counter += 1
            first_max = k[i]
    print(counter)
n = int(input())
func(n)