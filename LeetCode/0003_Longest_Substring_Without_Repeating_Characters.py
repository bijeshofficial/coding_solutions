class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        empty_string = ''
        count = 0

        for i in s:
            if i not in empty_string:
                empty_string += i
                count = max(count, len(empty_string))
            else:
                in_string = empty_string.index(i)
                empty_string = empty_string[in_string+1:] + i
        return count