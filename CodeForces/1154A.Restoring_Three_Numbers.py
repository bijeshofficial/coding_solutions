def func(n):
    n.sort()
    print(n[3]-n[0],n[3]-n[1],n[3]-n[2])
n = list(map(int,input().split()))
func(n)