class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        for k, v in dictionary.items():
            if v > 1:
                return True
        return False