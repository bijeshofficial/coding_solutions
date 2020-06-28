x = list(map(int,input().split()))
n = x[0]
t = x[1]
l = [str(t) for x in range(n)]
ans = ''.join(l)
if t == 10:
    if (int('1'*(n-1)+ '0')) == 0:
        print(-1)
    else:
        print(int('1'*(n-1)+ '0'))
elif len(ans)>n:
    print(-1)
else:
    print(int(''.join(l)))