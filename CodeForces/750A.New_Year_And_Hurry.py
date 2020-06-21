def func(n):
    time = 240
    question = n[0]
    time_to_get_to_party = n[1]
    counter = -1
    i = 1
    while time_to_get_to_party <= time:
        time_to_get_to_party += 5*i
        i += 1
        counter += 1
        if counter >= question:
            print(counter)
            return
    print(counter)
n = list(map(int,input().split()))
func(n)