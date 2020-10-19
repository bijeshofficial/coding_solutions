class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        ans = []
        for i in s:
            if i == '(':
                counter += 1
            elif i == ')':
                ans.append(counter)
                counter -= 1
        ans.append(counter)
        return max(ans)
