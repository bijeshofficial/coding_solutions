def func(n):
    for i in range(n):
        inp = int(input())
        k = list(map(int,input().split()))
        k.sort()
        minimum = 1000
        for i in range(len(k)-1):
            if k[i+1]-k[i] < minimum:
                minimum = k[i+1]-k[i]
        print(minimum)
n = int(input())
func(n)