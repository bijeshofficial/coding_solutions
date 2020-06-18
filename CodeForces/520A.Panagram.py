def func(n):
    k = input()
    if n < 26:
        print('NO')
        return
    k = set(k.lower())
    if len(k) != 26:
        print('NO')
        return
    print('YES')
n = int(input())
func(n)