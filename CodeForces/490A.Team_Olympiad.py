def func(n):
    m = list(map(int,input().split()))
    p = []
    math = []
    pe = []
    for i in range(len(m)):
        if m[i] == 1:
            p.append(i+1)
        elif m[i] == 2:
            math.append(i+1)
        else:
            pe.append(i+1)
    print((min(len(p),len(math),len(pe))))
    while p and math and pe:
        print(p.pop(),math.pop(),pe.pop())
            
n = int(input())
func(n)