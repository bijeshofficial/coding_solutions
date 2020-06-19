def func(n):
    dictionary = {}
    for i in range(n):
        k = input()
        if k not in dictionary:
            print('OK')
            dictionary[k] = 0
        else:
            dictionary[k] += 1
            print(k + str(dictionary[k]))
        print(dictionary)
n = int(input())
func(n)