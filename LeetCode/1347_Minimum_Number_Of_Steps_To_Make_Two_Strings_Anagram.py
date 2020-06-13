class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dictionary = {}
        counter = 0
        for i in s:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        for i in t:
            if i in dictionary and dictionary[i] > 0:
                dictionary[i] -=1
            else:
                counter += 1
        return counter