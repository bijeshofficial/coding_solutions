class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        length = -1
        for i in range(len(s)):
            for j in range(1, len(s)):
                if s[i] == s[j]:
                    length = max(length, j-i-1)
        return length
