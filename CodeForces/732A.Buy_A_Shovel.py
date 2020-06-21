def func(n):
    amount = n[0]
    spare = n[1]
    for i in range(1,11):
        if i * amount % 10 == 0 or i * amount % 10 == spare:
            print(i)
            return
n =list(map(int,input().split()))
func(n)