class Solution:
    def reverseWords(self, s: str) -> str:
        s= s.split()
        empty_list = []
        for i in s:
            empty_list.append(i[::-1])
        return ' '.join(empty_list)