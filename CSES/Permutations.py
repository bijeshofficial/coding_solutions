def p(n):
    e = [x for x in range(1,n+1) if x%2 ==0]
    o = [x for x in range(1,n+1) if x%2 != 0]
    if n == 1:
        print(1)
        return
    if n < 4:
        print ("NO SOLUTION")
        return
    a = e + o
    for i in a:
        print(i, end=" ")
n = int(input())
p(n)

# 2020-06-13 21:08:15	
# Python3	
# 0.63 s	
# 168 ch.