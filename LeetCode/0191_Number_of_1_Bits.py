class Solution:
    def hammingWeight(self, n: int) -> int:
        a = f'{int(str(n)):b}'
        return str(a).count('1')