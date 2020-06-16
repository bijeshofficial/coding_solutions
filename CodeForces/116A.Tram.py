def tram(n):
    maximum = 0
    counter = 0
    list_1 = []
    for i in range(n):
        k = list(map(int,input().split()))
        list_1.append(k)
    for i in list_1:
        counter -= i[0]
        counter += i[1]
        if counter > maximum:
            maximum = counter
    print(maximum)
n = int(input())
tram(n)