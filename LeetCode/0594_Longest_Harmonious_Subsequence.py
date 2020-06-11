class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        list_1 = []
        counter = 0
        for i in range(len(nums)-1):
            if abs(nums[i] - nums[i+1]) == 1:
                counter += nums.count(nums[i])
                counter += nums.count(nums[i+1])
            list_1.append(counter)
            counter = 0
        if len(nums)<=1:
            return 0
        return max(list_1)