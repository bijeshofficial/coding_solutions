b = int(input())
bs = list(map(int,input().split()))
g = int(input())
gs = list(map(int,input().split()))
bs.sort()
gs.sort()
counter = 0
i = 0
j = 0
while i != len(bs) and bs and gs:
    if bs[i] == gs[j] or abs(bs[i] - gs[j]) == 1:
        counter += 1
        bs.pop(i)
        gs.pop(j)
        j = 0
    else:
        j += 1
    if j:
        if j == len(gs):
            j = 0
            i += 1
print(counter)