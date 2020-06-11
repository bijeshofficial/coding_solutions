class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A = [str(x) for x in A]
        A = ''.join(A)
        C = int(A) + K
        D = [int(x) for x in str(C)]
        return D
