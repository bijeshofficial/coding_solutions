class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        counter = 0
        while n-i >= 0:
            n -= i
            i += 1
            counter += 1
        return counter