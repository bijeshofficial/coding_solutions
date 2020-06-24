def func(n):
    for i in range(n):
        k = list(map(int,input().split()))
        print(min(2,k[0]-1)*k[1])
n = int(input())
func(n)