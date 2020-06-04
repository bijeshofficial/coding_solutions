class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dictionary = {}
        list_1 = []
        for i in arr:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        print(dictionary)
        for k,v in dictionary.items():
            if k == v:
                list_1.append(k)
        if list_1:
            return max(list_1)
        return -1