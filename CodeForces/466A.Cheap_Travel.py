def func(k):
    n = k[0] #number of times she needs to use the train
    m = k[1] #special rides
    a = k[2] #cost of one subway tickets
    b = k[3] #cost of m rides
    #to print the minimum sum in rubles that Ann will need to spend
    if m * a <= b:
        print(n*a)
    else:
        print((n//m*b) + min((n%m)*a,b))
#         print((n//m*b) + (n%m)*a)
k = list(map(int,input().split()))
func(k)