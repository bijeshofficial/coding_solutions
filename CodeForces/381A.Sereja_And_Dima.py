def func(n):
    l = list(map(int,input().split()))
    s = 0
    d = 0
    start = 0
    end = len(l)-1
    for i in range(n//2):
#         print(s,d)
        s += max(l[start],l[end])
        if l[start]>l[end]:
            start += 1
        else:
            end -= 1
        d += max(l[start],l[end])
        if l[start]>l[end]:
            start += 1
        else:
            end -= 1
    if n%2 != 0:
        print(s+l[start],d)
    else:
        print(s,d)
n = int(input())
func(n)