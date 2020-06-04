class Solution:
    def fib(self, N: int) -> int:
        n1 = 0
        n2 = 1
        for i in range(N):
            temp = n1+n2
            n1 = n2
            n2 = temp
        return n1
        