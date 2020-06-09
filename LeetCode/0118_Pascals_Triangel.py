class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list_1 = []
        list_1.append([1]) 
        list_1.append([1,1])
        empty_list = []
        summe = 0
        j = 1
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        for i in range(numRows-2):
            x , y = 0 , 1
            empty_list.append(1) 
            for i in range(j):
                summe += list_1[-1][x] + list_1[-1][y]
                empty_list.append(summe)
                summe = 0
                x = y
                y += 1
            j+=1
            empty_list.append(1)
            list_1.append(empty_list)
            empty_list = [] 
        return list_1