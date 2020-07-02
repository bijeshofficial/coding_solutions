def func(n):
    for i in range(n):
        k= int(input())
        l = list(map(int,input().split()))
        print(len(set(l)))
n = int(input())
func(n)