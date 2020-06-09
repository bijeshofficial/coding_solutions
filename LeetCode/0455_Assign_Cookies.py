class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        counter = 0
        s.sort()
        g.sort()
        while s and g:
            if s[-1] >= g[-1]:
                s.pop()
                counter += 1
            g.pop()
        return counter