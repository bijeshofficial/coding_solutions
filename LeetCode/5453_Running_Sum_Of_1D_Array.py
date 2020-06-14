class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list_1 = []
        for i in range(len(nums)):
            list_1.append(nums[i]+sum(nums[:i]))
        return list_1