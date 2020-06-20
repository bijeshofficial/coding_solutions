def func(n):
    red_socks = n[0]
    blue_socks = n[1]
    different_counter = 0
    remainig_counter = 0
    while red_socks != 0 and blue_socks != 0:
#         print(red_socks,blue_socks)
        red_socks -= 1
        blue_socks -= 1
        different_counter += 1
    while blue_socks >= 2:
        blue_socks -= 2
        remainig_counter += 1
    while red_socks >= 2:
        red_socks -= 2
        remainig_counter += 1
    print(different_counter,remainig_counter)
n = list(map(int,input().split()))
func(n)