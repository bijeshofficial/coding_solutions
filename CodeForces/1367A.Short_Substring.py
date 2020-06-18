def short(n):
    for i in range(n):
        k = input()
        ans = ''
        ans += k[0]
        for i in range(len(k)):
            if i% 2 != 0:
                ans += k[i]
        print(ans)
n = int(input())
short(n)