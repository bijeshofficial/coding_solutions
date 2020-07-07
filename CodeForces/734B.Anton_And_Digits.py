def func(n):
    sume = 0
    two = n[0]
    three = n[1]
    five = n[2]
    six = n[3]
    while two and five and six:
        sume += 256
        two -= 1
        five -= 1
        six -= 1
    while two and three:
        sume += 32
        two -= 1
        three -= 1
    print(sume)
n = list(map(int,input().split()))
func(n)