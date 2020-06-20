def func(n):
    l = [100,20,10,5,1]
    counter = 0
    while n!= 0:
        if n%100 < n:
            counter +=1
            n-=100
        elif n%20 < n:
            counter +=1
            n-=20
        elif n%10 < n:
            counter +=1
            n-=10
        elif n%5 < n:
            counter +=1
            n-=5
        elif n%1 < n:
            counter += 1
            n-= 1
    print(counter)
n = int(input())
func(n)