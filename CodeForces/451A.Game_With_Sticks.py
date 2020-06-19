def func(n):
    counter = 0
    while n[0] != 0 and n[1] != 0:
        n[0] -= 1
        n[1] -= 1
        counter += 1      
    if counter % 2 == 0:
        print('Malvika')
    else:
        print('Akshat')
n = list(map(int,input().split()))
func(n)