class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty_dictionary = {}
        for index, value in enumerate(nums):
            remaining = target - value
            if remaining in empty_dictionary:
                return [empty_dictionary[remaining], index]
            empty_dictionary[value] = index
        return []