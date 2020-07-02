def func(n):
    for i in range(n):
        l = list(map(int,input().split()))
        to_get = l[0]
        n_of_odd_positive_integers = l[1]
        if to_get % 2 != 0 and n_of_odd_positive_integers % 2 == 0:
            print('NO')
        elif to_get % 2 == 0 and n_of_odd_positive_integers % 2 != 0:
            print('NO')
        elif n_of_odd_positive_integers**2 > to_get:
            print('NO')
        else:
            print('YES')            
n = int(input())
func(n)