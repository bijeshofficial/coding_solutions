def func(n):
    for i in range(n):
        l = list(map(int,input().split()))
        counter = 0
        while l[0] != 23:
            l[0] += 1
            counter += 60
        while l[1] != 60:
            l[1] += 1
            counter += 1
        print(counter)
n = int(input())
func(n)