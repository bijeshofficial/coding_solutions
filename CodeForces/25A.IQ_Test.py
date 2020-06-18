def func(n):
    k = list(map(int,input().split()))
    list_1 = []
    list_2 = []
    for i in k:
        if i % 2 == 0:
            list_1.append(i)
        else:
            list_2.append(i)
    if len(list_1) < len(list_2):
        print(k.index(list_1[0])+1)
    else:
        print(k.index(list_2[0])+1)
n = int(input())
func(n)