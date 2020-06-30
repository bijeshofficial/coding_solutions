def func(n):
    l = list(map(int,input().split()))   
    juicy = int(input())
    juicy_in = list(map(int,input().split()))
    dictionary = {}
    j = 1
    k = 1
    for i in l:
        for i in range(i):
            dictionary[j] = k
            j += 1
        k += 1
    for i in juicy_in:
        print(dictionary[i])
n = int(input())
func(n)