from math import ceil
def func(n):
    for i in range(n):
        k = int(input())
        l = list(map(int,input().split()))
        print(ceil(sum(l)/k))
n = int(input())
func(n)