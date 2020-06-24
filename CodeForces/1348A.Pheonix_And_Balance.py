def func(n):
    for i in range(n):
        k = int(input())
        l= [2**x for x in range(1,k+1)]
        sum_1 = sum(l[:(k//2)-1]) + l.pop()
        sum_2 = sum(l[(k//2)-1:])
        print(abs(sum_1-sum_2))
n = int(input())
func(n)