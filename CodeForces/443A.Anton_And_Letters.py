def func(n):
    l = set()
    for i in n:
        if i.isalpha():
            l.add(i)
    print(len(l))
n = input()
func(n)