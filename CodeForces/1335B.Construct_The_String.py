def func(n):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(n):
        ans = ''
        k = list(map(int,input().split()))
        length = k[0]
        unique = letters[:k[2]]
        # lenght_substring = k[1]
        ans += unique * (length//len(unique))
        i = 0
        while len(ans)!=length:
            ans += unique[i]
            i += 1
        print(ans)
n = int(input())
func(n)