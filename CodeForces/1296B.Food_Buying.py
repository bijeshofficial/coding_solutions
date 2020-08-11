def func(t):
    for i in range(t):
        n = int(input())
        counter = 0
        while n >= 10:
            to_add = n // 10
            counter += to_add*10
            n = n%10 + to_add
        counter += n
        print(counter)
t = int(input())
func(t)