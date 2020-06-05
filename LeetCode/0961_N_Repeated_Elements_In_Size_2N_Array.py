class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dictionary = {}
        for i in A:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1 
        for k,v in dictionary.items():
            if v == len(A)/2:
                return k