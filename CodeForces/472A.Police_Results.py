def func(n):
    k = list(map(int,input().split()))
    counter = 0
    recruited = 0
    for i in k:
        if recruited + i < 0:
            counter += 1
        else:
            recruited += i
    print(counter)
n = int(input())
func(n)