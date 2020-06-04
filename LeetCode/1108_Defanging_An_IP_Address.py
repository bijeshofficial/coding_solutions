class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer = ''
        for i in address:
            if i != '.':
                answer += i
            else:
                answer += '[.]'
        return answer