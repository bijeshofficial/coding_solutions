def func(t):
    for i in range(t):
        ans = []
        l2 = []
        n = int(input())
        l = list(map(int,input().split()))
        for i in l:
            if i not in ans and i not in l2:
                ans.append(i)
            else:
                l2.append(i)
        print(*ans)
t = int(input())
func(t)