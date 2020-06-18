def func(n):
    k = list(map(int,input().split()))
    percent = (sum(k)/(n*100))*100
    print(percent)   
n = int(input())
func(n)