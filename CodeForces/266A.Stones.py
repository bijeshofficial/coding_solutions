n = input()
k = input()
k = [x for x in k]
counter = 0
i = 0
while i < len(k)-1:
    if k[i] == k[i+1]:
        k.pop(i+1)
        counter += 1
    else:
        i += 1
print(counter)