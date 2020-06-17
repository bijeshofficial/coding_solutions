def even(n):
    counter = 0
    for i in range(n):
        x = list(map(int,input().split()))
        if abs(x[0] - x[1]) >= 2:
            counter += 1
    print(counter)
n = int(input())
even(n)