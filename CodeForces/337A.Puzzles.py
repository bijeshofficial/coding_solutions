def func(n):  
    x = list(map(int,input().split()))
    x.sort()
    count = 0
    maxi = x[0+n[0]-1]- x[0]
    for i in range(len(x)-n[0]+1):
        count = x[i+n[0]-1]- x[i]
        if count < maxi:
            maxi = count
    print(maxi)
n = list(map(int,input().split()))
func(n)