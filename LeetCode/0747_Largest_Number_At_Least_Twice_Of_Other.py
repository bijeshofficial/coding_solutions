class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a = max(nums)
        b = nums.index(a)
        nums[nums.index(a)] = 0
        for i in nums:
            if i > a/2:
                return -1
        return b