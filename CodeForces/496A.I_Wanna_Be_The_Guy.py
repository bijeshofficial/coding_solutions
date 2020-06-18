def func(n):
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    z = set(x for x in range(1,n+1))
    x = set(x[1:])
    y = set(y[1:])
    for i in z:
        if i not in x.union(y):
            print("Oh, my keyboard!")
            return
    print("I become the guy.")
n = int(input())
func(n)