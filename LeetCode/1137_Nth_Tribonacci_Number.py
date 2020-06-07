class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        for i in range(n-2):
            temp = a + b + c
            a , b , c = b, c, temp
        if n == 0:
            return 0
        if n == 1 or n==2:
            return 1
        return temp 