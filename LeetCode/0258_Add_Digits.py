class Solution:
    def addDigits(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        summe = 0
        while len(num) > 1:
            for i in range(len(num)):
                summe += num[i]
            return self.addDigits(summe)
        return num[0]


# O(1) Solution

# class Solution:
#     def addDigits(self, n: int) -> int:
#         if n == 0:
#             return n
#         x = n % 9
#         if x == 0:
#             return 9
#         return x