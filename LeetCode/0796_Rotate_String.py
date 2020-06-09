class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        for i in range(101):
            if A == B:
                return True
            A = A[1:] + A[0]
        return False