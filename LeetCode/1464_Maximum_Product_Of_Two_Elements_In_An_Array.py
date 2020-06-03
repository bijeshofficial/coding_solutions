class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max = max(nums)
        nums.remove(max(nums))
        second_max = max(nums)
        output = (first_max-1) * (second_max-1)
        return output