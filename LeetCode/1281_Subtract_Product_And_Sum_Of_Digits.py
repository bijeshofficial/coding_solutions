class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list_1 = [int(x) for x in str(n)]
        product = 1
        sume = 0
        for i in list_1:
            product *= i
        for i in list_1:
            sume += i
        return product - sume