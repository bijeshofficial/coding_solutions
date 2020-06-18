def func(n):
    initial_strength = n[0]
    l = []
    for i in range(n[1]):
        k = list(map(int,input().split()))
        l.append(k)
    l = sorted(l,key=lambda l:l[0])
    for i in range(len(l)):
        if l[i][0] < initial_strength:
            initial_strength += l[i][1]
        else:
            print('NO')
            return
    print('YES')
n = list(map(int,input().split()))
func(n)