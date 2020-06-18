from math import ceil
def func(n):
    even = n//2
    odd = ceil(n/2)
    e_sum = even*(even+1)
    o_sum = -(odd**2)
    main_sum = e_sum + o_sum
    print(main_sum)
n = int(input())
func(n)