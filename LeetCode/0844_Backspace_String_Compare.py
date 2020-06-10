class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        A = [x for x in S]
        B = [x for x in T]
        i = 0
        j = 0
        while '#' in A:
            if A[i] == '#' and i != 0:
                A.pop(i)
                A.pop(i-1)
                i = 0
            elif A[i] == '#':
                A.pop(i)
                i = 0
            else:
                i += 1
        while '#' in B:
            if B[j] == '#' and j != 0:
                B.pop(j)
                B.pop(j-1)
                j = 0
            elif B[j] == '#':
                B.pop(j)
                j = 0
            else:
                j += 1
        return A == B