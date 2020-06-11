class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        #Using Euclid-Euler Theorem
        p = [2,3,5,7,13,17,19,31]
        for i in p:
            if (2**(i-1))*((2**i) -1) == num:
                return True
        return False