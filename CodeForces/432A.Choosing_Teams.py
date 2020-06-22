def func(n):
    k = list(map(int,input().split()))
    counter = 0
    times_to_participate = n[1]
    for i in range(len(k)):
        if (5-k[i] >= times_to_participate):
            counter += 1
    print(counter//3)
n = list(map(int,input().split()))
func(n)