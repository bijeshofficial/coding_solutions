a = int(input())
height = 0
length = 1
i = 2
while (length) <= a:
    length += i*(i+1)/2
    height += 1
    i += 1
print(height)