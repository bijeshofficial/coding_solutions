def func(n):
    for i in range(n):
        k = list(map(int,input().split()))
        a = k[0]
        b = k[1]
        length = min(a,b) * 2
        width = max(a,b)
        if width < length:
            width += abs(length - width)
        else:
            length += abs(length - width)
        print(length*width)
n = int(input())
func(n)