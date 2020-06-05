class Solution:
    def generateTheString(self, n: int) -> str:
        a = 'a'
        b = 'b'
        c = 'c'
        ans = ''
        if n%2 == 0:
            ans += a*1
            ans += b*(n-1)
        else:
            ans += c*n
        return ans