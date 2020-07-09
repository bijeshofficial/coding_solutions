def func(n):
    maximum = max(n)
    if max(n)== 1:
        print('1/1')
    elif max(n) == 2:
        print('5/6')
    elif max(n) == 3:
        print('2/3')
    elif max(n) == 4:
        print('1/2')
    elif max(n) == 5:
        print('1/3')
    else:
        print('1/6')
n = list(map(int,input().split()))
func(n)