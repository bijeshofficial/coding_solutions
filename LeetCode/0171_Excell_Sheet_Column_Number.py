class Solution:
    def titleToNumber(self, s: str) -> int:
        mul = 1
        sume = 0
        for i in range(len(s)-1,-1,-1):
            sume += mul*(ord(s[i])-64)
            mul *= 26
        return sume