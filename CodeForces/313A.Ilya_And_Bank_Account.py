def func(n):
    if n > 0:
        print(n)
    else:
        l = [x for x in str(n)]
        temp1 = l.copy()
        temp2 = l.copy()
        temp1.pop()
        temp2.pop(-2)
        if ''.join(temp1) == '-0':
            print(0)
            return
        elif ''.join(temp2) == '-0':
            print(0)
            return
        if int(''.join(temp1)) > int(''.join(temp2)):
            print(''.join(temp1))
        else:
            print(''.join(temp2))
n = int(input())
func(n)