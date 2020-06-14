n = int(input())
for i in range(n):
    k = input()
    if len(k) > 10:
        print(k[0] + str(len(k)-2) + k[-1])
    else:
        print(k)