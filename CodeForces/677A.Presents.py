def func(n):
    x = list(map(int,input().split()))
    dictionary = {}
    l = []
    j = 1
    for i in x:
        dictionary[j] = i
        j += 1
    x = 1
    while len(l) < n:
        for k,v in dictionary.items():
            if v == x:
                l.append(k)
                x+= 1
    for i in l:
        print(i, end= ' ')
n = int(input())
func(n)