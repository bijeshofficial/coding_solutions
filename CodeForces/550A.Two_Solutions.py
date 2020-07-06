def func(n):
    if 'AB' not in n or 'BA' not in n:
        print('NO')
        return
    a = n.index('AB')
    b = n.index('BA')
    for i in range(a+2,len(n)-1):
        if n[i]+n[i+1] == 'BA':
            print('YES')
            return
    for i in range(b+2,len(n)-1):
        if n[i]+n[i+1] == 'AB':
            print('YES')
            return
    print('NO')
n = input()
func(n)