def func(n):
    if n.isupper():
            print(n.lower())
            return
    if n[0].islower() and n[1:].isupper():
        print(n[0].upper() + n[1:].lower())
    elif len(n) == 1 and n.islower():
        print(n.upper())
    else:
        print(n)
n = input()
func(n)