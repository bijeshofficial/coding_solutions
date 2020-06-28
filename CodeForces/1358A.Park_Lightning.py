from math import ceil
x = int(input())
for i in range(x):
    y = list(map(int,input().split()))
    print(ceil((y[0]*y[1])/2))