def func(n):
    a = n[0]
    b = n[1]
    heap_of_stones = n[2]
    
    while heap_of_stones >= 0:
        i = a
        while i > 0:
            if heap_of_stones % i == 0 and a % i == 0:
                heap_of_stones -= i
                break
            else:
                i -= 1
        if heap_of_stones == 0:
            print(0)
            return
        j = b
        while j > 0:
            if heap_of_stones % j == 0 and b % j == 0:
                heap_of_stones -= j
                break
            else:
                j -= 1
        if heap_of_stones == 0:
            print(1)
            return
n = list(map(int,input().split()))
func(n)