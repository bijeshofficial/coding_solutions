class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = {}
        for i in arr:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        return len(set(dictionary.values())) == len(dictionary.values())