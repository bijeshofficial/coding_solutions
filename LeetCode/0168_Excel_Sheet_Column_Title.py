class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        while n:
            first = (n-1)%26
            ans += chr(first + 65)
            n = (n -1) //26
        return ans[::-1]