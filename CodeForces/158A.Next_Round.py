n = list(map(int,input().split()))
m = list(map(int,input().split()))
k = n[1]
score = m[k-1]
counter = 0
for i in m:
    if i > 0 and i >= score:
        counter += 1
print(counter)