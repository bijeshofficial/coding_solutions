def func(num):
    for i in range(num):
        y = [1 for x in range(int(input()))]
        print(*y)
num = int(input())
func(num)