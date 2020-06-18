def func(n):
    k = list(map(int,input().split()))
    x = min(k)
    y = max(k)
    counter_to_end = 0
    counter_to_front = 0
    largest_index_of_min = 0
    smallest_index_of_max = len(k)-1
    for i in range(len(k)):
        if k[i] == min(k):
            temp = i
            if temp > largest_index_of_min:
                largest_index_of_min = temp
        if k[i] == max(k):
            tempo = i
            if tempo < smallest_index_of_max:
                smallest_index_of_max = tempo
#     print(largest_index_of_min,smallest_index_of_max)
    if smallest_index_of_max < largest_index_of_min:
        counter_to_end = abs(largest_index_of_min - (len(k)-1))
        counter_to_front = smallest_index_of_max
        print(counter_to_end + counter_to_front)
    else:
        counter_to_end = abs(largest_index_of_min - (len(k) -1))
        counter_to_front = smallest_index_of_max
        print(counter_to_end+counter_to_front-1)
n = int(input())
func(n)