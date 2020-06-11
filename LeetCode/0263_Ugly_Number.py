class Solution:
    def isUgly(self, num: int) -> bool:
        while num >= 1:
            # print(num)
            if num %2 ==0:
                num /= 2
            elif num %3 ==0:
                num /=3
            elif num % 5 ==0:
                num /=5
            if num == 1:
                return True
            if num/2 ==1 or num/3 == 1 or num/5 ==1:
                return True
            elif num%2 != 0 and num%3 !=0 and num%5!=0:
                return False
        return False