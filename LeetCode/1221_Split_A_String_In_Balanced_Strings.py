class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_r = 0 
        count_l = 0
        counter = 0
        s = [x for x in s]
        for i in range(len(s)):
            if s[0] == 'R':
                count_r += 1
                s.pop(0)

            elif s[0] == 'L':
                count_l += 1
                s.pop(0)

            if count_r == count_l and count_r != 0 and count_l !=0:
                counter +=1

        return counter  