n = int(input())
counter = 0
for i in range(n):
    k = list(map(int,input().split()))
    if k.count(1) >=2:
        counter += 1
print(counter)