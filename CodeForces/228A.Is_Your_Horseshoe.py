def func(n):
    print(abs(len(set(n)) - len(n)))
n = list(map(int,input().split()))
func(n)