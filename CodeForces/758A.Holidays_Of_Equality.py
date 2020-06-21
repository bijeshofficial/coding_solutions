def func(n):
    k = list(map(int,input().split()))
    richest = max(k)
    counter = 0
    for i in k:
        if i != richest:
            counter += (richest - i)
    print(counter)
n = int(input())
func(n)