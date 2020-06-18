def even(n):
    for i in range(n):
        x = int(input())
        list_1 = list(map(int,input().split()))
        counter = 0
        even_count = 0
        odd_count = 0
#         odd_num = 0
#         even_num = 0
        for i in range(len(list_1)):
            if list_1[i]%2 == 0:
                even_count += 1
            else:
                odd_count += 1
        if even_count < odd_count:
            print(-1)
        elif abs(even_count - odd_count) > 1:
            print(-1)
        else:
            for i in range(len(list_1)):
#                 if list_1[i]%2 == 0 and i % 2 == 0:
#                     continue
#                 elif list_1[i]%2 != 0 and i % 2 != 0:
#                     continue
                if list_1[i] %2 ==0 and i % 2 != 0:
                    counter += 1
                elif list_1[i] % 2 != 0 and i % 2 == 0:
                    counter += 1
            print(counter//2)
n = int(input())
even(n)