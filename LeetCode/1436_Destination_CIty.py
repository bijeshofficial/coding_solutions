class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dictionary = {}
        for i,j in paths:
            dictionary[i] = j
        for i in paths:
            for j in i:
                if j in dictionary.values() and j not in dictionary.keys():
                    return j