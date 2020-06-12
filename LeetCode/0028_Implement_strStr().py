class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)< 1 and len(needle)<1:
            return 0
        for i,v in enumerate(haystack):
            if haystack[i:i+len(needle)] == needle:
                 return i
        return -1