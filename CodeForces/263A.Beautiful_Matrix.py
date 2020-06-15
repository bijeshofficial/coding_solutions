l = []
for i in range(5):
    k = list(map(int,input().split()))
    l.append(k)
for i in range(5):
    for j in range(5):
        if l[i][j] == 1:
            first = i
            second = j
print(abs(first-2)+abs(second-2))