def bear(n):
    a = n[0]
    b = n[1]
    years = 0
    while a <= b:
        a *= 3
        b *= 2
        years += 1
    print(years)
n = list(map(int,input().split()))
bear(n)