def func(k):
    n = list(map(int,input().split()))
    n.sort()
    maximum = 0
    if 0 in n and k[1] in n:
        for i in range(len(n)-1):
            temp = n[i+1] - n[i]
            if (temp) > maximum:
                maximum = temp
        print(maximum/2)
        return
    else:
        if 0 not in n:
            n.insert(0,0)
        if k[1] not in n:
            n.append(k[1])
            last_difference = n[-1] - n[-2]
        else:
            last_difference = n[-1] - k[1]
        # print(n)
        difference_zero = n[1] - n[0]
        temp = max(difference_zero,last_difference)
        # print(difference_zero, last_difference,temp)
        for i in range(len(n)-1):
            if (n[i+1] - n[i])/2 > temp:
                temp = (n[i+1] - n[i])/2
        if (temp/2) >= max(difference_zero,last_difference)/2:
            print(temp)
        else:
            print(temp/2)
k =list(map(int,input().split()))
func(k)