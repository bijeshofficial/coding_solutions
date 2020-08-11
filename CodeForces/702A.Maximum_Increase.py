def func(t):
    a = list(map(int, input().split()))
    l = []
    counter = 0
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            counter += 1
        else:
            l.append(counter)
            counter = 0
    l.append(counter)
    print(max(l)+1)
t = int(input())
func(t)