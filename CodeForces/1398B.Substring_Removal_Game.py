def func(s):
    for i in range(s):
        n = input()
        alice = 0
        ans = ''
        l = []
        for i in n:
            if i == '1':
                ans += '1'
            elif i == '0' and len(ans) >= 1:
                l.append(ans)
                ans = ''
            else:
                continue
        print(l)
        l.append(ans)
        l.sort(reverse=True)
        l = l[::2]
        print(l)
        for i in l:
            alice += len(i)
        print(alice)


s = int(input())
func(s)
