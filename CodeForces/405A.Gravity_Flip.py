def func(n):
    x = list(map(int,input().split()))
#     for i in sorted(x):
#         print(i,end= ' ')
    print(' '.join(map(str,sorted(x))))
n = int(input())
func(n)