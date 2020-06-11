class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        square = 1
        i = 0
        while square <= n:
            if 2**i == n:
                return True
            else:
                i+=1
                square = 2**i
        return False