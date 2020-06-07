class Solution:
    def countBits(self, num: int) -> List[int]:
        empty_list = []
        for i in range(num+1):
            j = f'{i:b}'
            empty_list.append(j.count('1'))
        return empty_list