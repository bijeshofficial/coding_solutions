def func(x,y):
    s = ''
    for i in range(len(x)):
        s += str(int(x[i])^int(y[i]))
    print(s)
x = input()
y = input()
func(x,y)