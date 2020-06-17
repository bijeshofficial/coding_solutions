def func(n):
    x = 'I hate that'
    y = 'I love that'
    ans = ''
    if n == 1:
        print('I hate it')
        return
    for i in range(n):
        if i % 2 == 0:
            ans += x + ' '
        else:
            ans += y + ' '
    ans = ans[:-5] + 'it'
    print(ans)
n = int(input())
func(n)