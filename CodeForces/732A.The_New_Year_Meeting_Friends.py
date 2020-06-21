def func(n):
    n.sort()
    distance = 0
    distance += n[1]-n[0]
    distance += n[2] - n[1]
    print(distance)
n = list(map(int,input().split()))
func(n)