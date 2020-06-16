n = int(input())
m = 5
counter = 0
while n != 0:
    if n >= m:
        n -= m
        counter += 1
    else:
        m -= 1
print(counter)