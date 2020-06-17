n = int(input())
g = list(map(int,input().split()))
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for i in g:
    if i == 1:
        count_1 += 1
    elif i == 2:
        count_2 += 1
    elif i == 3:
        count_3 += 1
    elif i == 4:
        count_4 += 1
min_count = count_4
while count_1 != 0 and count_3 != 0:
    count_1 -= 1
    count_3 -= 1
    min_count += 1
if count_1 == 0 and count_3 != 0:
    min_count += count_3
    count_3 = 0
min_count += count_2//2
if count_2 % 2 != 0:
    if count_1 <=2:
        min_count += 1
        count_1 =0
        count_2 = 0
    else:
        count_1 -= 2
        count_2 = 0
        min_count += 1
if count_1 != 0:
    min_count += count_1/4
    if count_1 % 4 != 0:
        min_count += 1
print(int(min_count))