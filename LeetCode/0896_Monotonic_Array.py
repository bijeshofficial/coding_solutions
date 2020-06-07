class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        B = sorted(A, reverse = True)
        C = sorted(A)
        return B == A or C == A