class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        n = n-1
        a = 1
        while str(n).count('0')>0 or str(a).count('0')>0:
            n -= 1
            a += 1
        return [a,n]