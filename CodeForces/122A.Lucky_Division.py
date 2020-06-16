def lucky(n):
    m = [4,7,47,74,447,474,774,747,777,444,744,774,747,477]
    if n in m:
        print('YES')
        return
    for i in m:
        if n % i == 0:
            print('YES')
            return
    print('NO')
n = int(input())
lucky(n)