def func(n):
    height = n[0]
    length = n[1]
    counter = 0
    for i in range(height):
        if i%2 == 0:
            print('#'*length)
        elif i%2 != 0 and counter%2 == 0:
            print('.'*(length-1) + '#')
            counter += 1
        elif i%2 != 0 and counter%2 != 0:
            print('#' + '.' * (length-1) )
            counter += 1
n = list(map(int,input().split()))
func(n)