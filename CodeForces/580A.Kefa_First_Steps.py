def func(n):
    counter = 0
    maxi = 0
    x = list(map(int,input().split()))
    for i in range(len(x)-1):
        if x[i] <= x[i+1]:
            counter += 1
            if counter > maxi:
                maxi = counter
        else:
            counter = 0
    print(maxi + 1)
n = int(input())
func(n)