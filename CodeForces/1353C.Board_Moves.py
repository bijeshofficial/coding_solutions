def func(n):
    for i in range(n):
        k = int(input())
        ans = 0
        for i in range(1,k//2+1):
            ans += i * i
        print(ans*8)
n = int(input())
func(n)