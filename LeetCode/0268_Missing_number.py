class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        if nums[0] != 0:
            return 0
        while nums:
            if len(nums)>1:
                if abs(nums[i] - nums[i+1]) == 1:
                    nums.pop(i)
                    continue
                else:
                    return nums[i] + 1
            return nums[i] + 1