class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 2
        temp = 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(n-2):
                temp = n1+n2
                n1 = n2
                n2 = temp
        return temp