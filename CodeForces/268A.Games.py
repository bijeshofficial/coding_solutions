def func(n):
    l = []
    for i in range(n):
        k = list(map(int,input().split()))
        l.append(k)
    counter = 0
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][0] == l[j][1]:
                counter += 1
    print(counter)
n = int(input())
func(n)