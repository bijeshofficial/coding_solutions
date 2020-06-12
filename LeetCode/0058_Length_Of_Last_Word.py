class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        if s:
            return len(s.pop())
        return 0