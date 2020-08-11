def func(t):
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        counter = 0
        for i in range(n):
            counter += max(a[i]-min(a), b[i]-min(b))
        print(counter)               
t = int(input())
func(t)