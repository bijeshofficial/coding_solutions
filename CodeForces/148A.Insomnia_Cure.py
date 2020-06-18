k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
li = [x for x in range(1,d+1)]
main = []
for i in li:
    if (i % k == 0) or (i % l == 0) or (i % m == 0) or (i % n == 0):
        main.append(i)
print(len(main))