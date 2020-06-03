class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(6): # can use any number
            addition = 0
            n = [int(x) for x in str(n)]
            for j in n:
                addition += j**2
            if addition == 1:
                return True
            else:
                n = addition
                addition = 0
        return False