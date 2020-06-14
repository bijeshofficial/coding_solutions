n = int(input())
m = input()
list_1 = [int(b) for b in m.split()]
counter = 0
for i in range(1,len(list_1)):
    if list_1[i] < list_1[i-1]:
        counter += list_1[i-1] - list_1[i]
        list_1[i] = list_1[i-1]
print(counter)

# 2020-06-13 20:47:29	
# Python3	
# 0.11 s	
# 178 ch.