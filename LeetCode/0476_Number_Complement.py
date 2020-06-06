class Solution:
    def findComplement(self, num: int) -> int:
        answer = ''
        binary = f'{num:b}'
        for i in binary:
            if i == '1':
                answer += '0'
            else:
                answer += '1'
        return int(answer,2)