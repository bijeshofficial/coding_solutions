class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0 and x <= 2**31-1:
            list1 = list(str(x))
            x = int(''.join(list1)[::-1])
            if x < 2**31-1:
                return x
            else:
                return 0
        elif x < 0 and x >= -2**31:
            list1 = list(str(x))
            list1.remove('-')
            x = int(''.join(list1)[::-1])
            ans = - + x
            if ans > -2**31:
                return ans
            else:
                return 0
        else:
            return 0