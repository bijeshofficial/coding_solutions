def func(n):
    x = (n.split('WUB'))
    y = ''
    for i in x:
        if i != '':
            y += i + ' '

    print(y.rstrip())
n = input()
func(n)