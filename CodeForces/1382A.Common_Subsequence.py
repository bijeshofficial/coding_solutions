def func(t):
    for i in range(t):
        a= list(map(int,input().split()))
        n = list(map(int,input().split()))
        m = list(map(int,input().split()))
        flag = True
        for i in range(len(n)):
            if n[i] in m:
                print('YES')
                print(1, n[i])
                flag = False
                break
        if flag:
            print('NO')
t = int(input())
func(t)