def func(n):
    m = 0
    c = 0 
    for i in range(n):
        k = list(map(int,input().split()))
        if k[0] > k [1]:
            m += 1
        elif k [1] > k [0]:
            c += 1
    if m > c:
        print('Mishka')
    elif c > m:
        print('Chris')
    else:
        print('Friendship is magic!^^')
n = int(input())
func(n)