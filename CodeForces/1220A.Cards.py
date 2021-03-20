def func(n, l):
    ans = ''
    count_of_zero = l.count('z')
    count_of_one = l.count('n')
    for i in range(count_of_one):
        ans += '1 '
    for i in range(count_of_zero):
        ans += '0 '
    return ans


number = int(input())
letter = input()
print(func(number, letter))
