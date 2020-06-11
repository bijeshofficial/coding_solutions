class Solution:
    def trailingZeroes(self, n: int) -> int:
        five = 5
        zeros = 0
        while n >= five:
            zeros += n // five
            five *= 5
        return zeros   