def chat(s):
    list_1 = [x for x in s]
    list_2 = []
    i = 0
    while list_1:
        if len(list_2) == 0:
            if list_1[i] == 'h':
                list_2.append(list_1.pop(0))
            else:
                list_1.pop(0)
        elif len(list_2) == 1:
            if list_1[i] == 'e':
                list_2.append(list_1.pop(0))
            else:
                list_1.pop(0)
        elif len(list_2) == 2:
            if list_1[i] == 'l':
                list_2.append(list_1.pop(0))
            else:
                list_1.pop(0)
        elif len(list_2) == 3:
            if list_1[i] == 'l':
                list_2.append(list_1.pop(0))
            else:
                list_1.pop(0)
        elif len(list_2) == 4:
            if list_1[i] == 'o':
                list_2.append(list_1.pop(0))
            else:
                list_1.pop(0)
        else:
            list_1.pop(0)
    if ''.join(list_2) == 'hello':
        print('YES')
    else:
        print('NO')
        
s = input()
chat(s)