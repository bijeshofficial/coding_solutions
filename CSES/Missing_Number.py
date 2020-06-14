n = int(input())
m = input()
list_1 = [int(x) for x in m.split()]
sume = sum(x for x in range(1,n+1))
ans = sume - sum(list_1)
print(ans)

#2020-06-14 11:30:04
#Python3
#0.11 s
#112 ch.
