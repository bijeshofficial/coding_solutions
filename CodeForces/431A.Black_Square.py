def func(n):
    l = input()
    counter = 0
    for i in l:
        counter += n[int(i)-1]
    print(counter)
n = list(map(int,input().split()))
func(n)