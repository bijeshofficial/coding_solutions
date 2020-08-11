def func(t):
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        flag = True
        for i in range(len(a)-1):
            if abs(a[i] - a[i+1]) > 1:
                print('NO')
                flag = False
                break
        if flag:
            print('YES')                
t = int(input())
func(t)