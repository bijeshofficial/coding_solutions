n = list(map(int,input().split()))
q = input()
q = [x for x in q]
for i in range(n[1]):
    j = 0
    while j < len(q)-1:
        if q[j] == 'B' and q[j+1] == 'G':
            temp = q[j]
            q[j] = q[j+1]
            q[j+1] = temp
            j += 2
        else:
            j += 1
print(''.join(q))