class Solution:
    def reformat(self, s: str) -> str:
        alpha = []
        nume = []
        ans = []
        for i in s:
            if i.isalpha():
                alpha.append(i)
            else:
                nume.append(i)
        if abs(len(alpha) - len(nume)) > 1:
            return ''
        if len(alpha) >= len(nume):
            while nume:
                ans.append(alpha.pop())
                ans.append(nume.pop())
            while alpha:
                ans.append(alpha.pop())
        else:
            while alpha:
                ans.append(nume.pop())
                ans.append(alpha.pop())
            while nume:
                ans.append(nume.pop())
        return ''.join(ans)