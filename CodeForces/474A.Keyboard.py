def func(n):
    string = 'qwertyuiopasdfghjkl;zxcvbnm,./'
    k = input()
    ans = ''
    for i in k:
        if n == 'R':
            ans += string[string.index(i)-1]
        else:
            ans += string[string.index(i)+1]
    print(ans)
n = input()
func(n)