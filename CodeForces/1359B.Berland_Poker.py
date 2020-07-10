def func(n):
    for i in range(n):
        l = list(map(int,input().split()))
        cards = l[0] #n
        joker = l[1] #m
        players = l[2] #k
        if joker == 0:
            print(0)
            continue
        else:
            d = []
            cards_to_give = cards//players
            for i in range(players):
                d.append(0)
            if joker < cards_to_give:
                print(joker)
                continue
            else:
                d[0] += cards_to_give
                joker -= cards_to_give
                j = 1
                while joker >  0:
                    d[j] += 1
                    joker -= 1
                    j += 1
                    if j == len(d):
                        j = 1
            # print(d)
            first = 0
            second = 0
            if len(d) >= 2:
                first += max(d)
                d[d.index(max(d))] = 0
                second += max(d)
                print(first-second)
            else:
                print(max(d))
n = int(input())
func(n)

# Actual Logic. 
# Don't know what i was thinking when I wrote the above code.
# print(min(m,(n-m)//(k-1)))
