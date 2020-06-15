n = int(input())
x = 0
for i in range(n):
    y = input()
    if '++' in y:
        x += 1
    elif '--' in y:
        x -= 1
print(x)