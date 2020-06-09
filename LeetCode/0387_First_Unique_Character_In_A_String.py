class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        if len(set(s)) == 0 or not s:
            return -1
        
        for i, v in enumerate(s):
            if s.count(v) == 1:
                return i
        return -1