class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        mini = 0
        for i in range(0,len(nums),2):
            minimum = min(nums[i] , nums[i+1])
            mini+=minimum
        return mini