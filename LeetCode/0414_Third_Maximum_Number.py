class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums)>=3:
            nums.pop()
            nums.pop()
            return nums[-1]
        else:
            return max(nums)