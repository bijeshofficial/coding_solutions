n = list(map(int,input().split()))
cost_banana = n[0]
dollar = n[1]
total = 0
for i in range(1,n[2]+1):
    total += i*cost_banana
if total-dollar < 0:
    print(0)
else:
    print(total-dollar)