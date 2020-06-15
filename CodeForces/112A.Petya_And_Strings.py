def petya(a,b):
    a , b = a.lower(), b.lower()
    for i in range(len(a)):
        if ord(a[i]) != ord(b[i]):
            if ord(a[i]) > ord(b[i]):
                print(1)
                return
            elif ord(a[i])<ord(b[i]):
                print(-1)
                return
    print(0)
a = input()
b = input()
petya(a,b)