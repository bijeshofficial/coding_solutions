def word(n):
    count_lower = 0
    count_upper = 0
    for i in n:
        if i.islower():
            count_lower += 1
        else:
            count_upper += 1
    if count_lower > count_upper:
        n = n.lower()
    elif count_lower < count_upper:
        n = n.upper()
    else:
        n = n.lower()
    print(n)
n = input()
word(n)