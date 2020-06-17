def nearly(n):
    counter = 0
    for i in str(n):
        if i == '4' or i == '7':
            counter += 1
    for i in str(counter):
        if i != '4' and i != '7':
            print('NO')
            return
    print('YES')
n = int(input())
nearly(n)