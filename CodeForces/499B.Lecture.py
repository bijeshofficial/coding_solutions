def func(n):
    dictionary = dict(input().split() for i in range(n[1]))
    print(dictionary)
    text = input().split()
    ans = []
    for i in text:
        ans.append(min(i,dictionary[i],key=len))
    print(' '.join(ans))
n = list(map(int,input().split()))
func(n)