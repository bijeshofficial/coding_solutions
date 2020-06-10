class Solution:
    def checkRecord(self, s: str) -> bool:
        counter = 0
        for i in s:
            if i == 'L':
                counter += 1
                if counter > 2:
                    return False
            elif i != 'L':
                counter = 0
        if s.count('A') > 1:
            return False
        return True