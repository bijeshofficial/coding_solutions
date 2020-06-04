class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        list_1 = []
        for i in A:
            if i%2 == 0:
                list_1.append(i)
        for i in A:
            if i % 2 != 0:
                list_1.append(i)
        return list_1