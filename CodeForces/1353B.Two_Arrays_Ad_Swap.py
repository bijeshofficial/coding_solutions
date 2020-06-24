def func(n):
    for i in range(n):
        m = list(map(int,input().split()))
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        max_swap = m[1]
        sume = 0
        a.sort(reverse = True)
        b.sort()
        while a[-1]<b[-1] and max_swap != 0:
            max_swap -= 1
            a.pop()
            sume += b.pop()
            if a == []:
                break
        print(sum(a)+ sume)
n = int(input())
func(n)