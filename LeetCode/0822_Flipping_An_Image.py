class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        empty_list = []
        new_list = []
        for i in A:
            i.reverse()
        for i in A:
            for j in i:
                if j == 1:
                    j = 0
                else:
                    j =1
                new_list.append(j)
            empty_list.append(new_list)
            new_list = []
        return empty_list