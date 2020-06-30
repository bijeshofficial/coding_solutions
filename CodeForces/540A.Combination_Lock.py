def func(n):
    k = list(map(int,input()))
    l = list(map(int,input()))
    counter = 0
    for i in range(n):
        counter += (min(abs(k[i]-l[i]),10-abs(k[i]-l[i])))
    print(counter)
n = int(input())
func(n)