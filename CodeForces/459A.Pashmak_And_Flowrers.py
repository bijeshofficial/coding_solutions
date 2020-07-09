def func(n):
    l = list(map(int,input().split()))
    bd = max(l) - min(l)
    if len(set(l)) == 1:
        print(bd,n*(n-1)//2)
    else:
        print(bd,l.count(max(l))*l.count(min(l)))
n = int(input())
func(n)