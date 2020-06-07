class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        a, b, c = A.pop(), A.pop(), A.pop()
        while b+c <= a:
            if A == []:
                return 0
            else:
                a, b, c = b, c ,A.pop()
        return a+b+c