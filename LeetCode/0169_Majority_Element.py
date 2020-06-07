class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        for k,v in dictionary.items():
            if v > len(nums)/2:
                return k