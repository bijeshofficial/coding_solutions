class Solution:
    def bitwiseComplement(self, N: int) -> int:
        N = f'{N:b}'
        ans = ''
        for i in N:
            if i == '1':
                ans += '0'
            else:
                ans += '1'
        return int(ans,2)