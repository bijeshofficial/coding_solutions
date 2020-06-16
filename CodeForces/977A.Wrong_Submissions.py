def wrong(n):
    number = n[0]
    times = n[1]
    for i in range(times):
        if str(number)[-1] == '0':
            number //= 10
        else:
            number -= 1
    print(number)
n = list(map(int,input().split()))
wrong(n)