def func(n):
    x = input()
    ans = 0
    l_counter = x.count('L')
    r_counter = x.count('R')
    y = 0 - l_counter
    z = 0 + r_counter
    for i in range(y,z+1):
        ans += 1
    print(ans)
n = int(input())
func(n)

# Actaully the answer was just
# No need to write such a long ans
n = int(input())
l = input()
print(n+1)