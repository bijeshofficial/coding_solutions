class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = 'qwertyuiopQWERTYUIOP'
        second_row = 'asdfghjklASDFGHJKL'
        third_row = 'zxcvbnmZXCVBNM'
        output = []
        for i in words:
            counter_first = 0
            counter_second = 0
            counter_third = 0
            for j in i:
                if j in first_row:
                    counter_first +=1
                elif j in second_row:
                    counter_second += 1
                elif j in third_row:
                    counter_third += 1
            if counter_first == len(i) or counter_second == len(i) or counter_third == len(i):
                output.append(i)
        return output