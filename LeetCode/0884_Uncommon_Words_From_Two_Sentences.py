class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split()
        B = B.split()
        list_1 = A+B
        output = []
        for i in list_1:
            if list_1.count(i) == 1:
                output.append(i)
        return output