def func(n):
    stairs = n[0]
    multiple = n[1]
    if multiple > stairs:
        print(-1)
        return
    if stairs % 2 == 0:
        total = stairs // 2
        while total % multiple != 0:
            total += 1
        if total % multiple != 0:
            print(-1)
        else:
            print(total)
        return
    else:
        total = (stairs // 2) + 1
        while total % multiple != 0:
            total += 1
        if total % multiple != 0:
            print(-1)
        else:
            print(total)
        return
n = list(map(int,input().split()))
func(n)