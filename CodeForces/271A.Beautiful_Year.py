def func(n):
    while True:
        n += 1 
        if str(n)[0] != str(n)[1] and str(n)[0] != str(n)[2] and str(n)[0] != str(n)[3]:
            if str(n)[1] != str(n)[2] and str(n)[1] != str(n)[3]:
                if str(n)[2] != str(n)[3]:
                    print(n)
                    return
n = int(input())
func(n)