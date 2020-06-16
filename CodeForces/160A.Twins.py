n = int(input())
coins = list(map(int,input().split()))
s = 0
sort_coins = sorted(coins)
while s <= sum(sort_coins):
    s += sort_coins[-1]
    sort_coins.pop()
print(len(coins) - len(sort_coins))