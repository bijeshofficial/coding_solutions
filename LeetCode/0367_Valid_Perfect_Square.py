class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        mul = 0
        while mul < num:
            mul = i* i
            i += 1 
            if mul == num:
                return True
        return False