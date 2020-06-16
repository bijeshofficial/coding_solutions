def hq9(n):
    for i in n:
        if i == 'H' or i == 'Q' or i == '9':
            print('YES')
            return
    print('NO')
    return
n = input()
hq9(n)