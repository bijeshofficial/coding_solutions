def func(n):
    for i in range(n[0]):
        k = list(map(str,input().split()))
        for i in k:
            if i in 'CMY':
                print('#Color')
                return
    print('#Black&White')
n = list(map(int,input().split()))
func(n)