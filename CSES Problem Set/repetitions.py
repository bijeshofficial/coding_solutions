def dna(n):
    counter = 1
    l = [1]
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            counter += 1
        else:
            l.append(counter)
            counter = 1
    l.append(counter)
    print(max(l))
n = input()
dna(n)

# 2020-06-13 20:12:00	
# Python3	
# 0.12 s	
# 147 ch.