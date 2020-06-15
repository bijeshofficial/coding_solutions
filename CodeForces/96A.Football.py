def football(n):
    for i in range(len(n)):
        if n[i:i+7] == '1111111' or n[i:i+7] == '0000000':
            print('YES')
            return
    print('NO')
n = input()
football(n)