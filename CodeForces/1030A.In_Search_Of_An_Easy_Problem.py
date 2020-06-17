def func(n):
    x= list(map(int,input().split()))
    for i in x:
        if i == 1:
            print('HARD')
            return 
    print('EASY')
n = int(input())
func(n)