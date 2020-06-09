class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = [x for x in s]
        t = [x for x in t]
        a = []
        while t and S:
            if S[-1] == t[-1]:
                a.append(t[-1])
                t.pop()
                S.pop()
            else:
                t.pop()
        a = a[::-1]
        return ''.join(a) == s