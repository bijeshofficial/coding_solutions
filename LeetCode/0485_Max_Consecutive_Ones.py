class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = []
        counter = 1
        if nums.count(1) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i] == 1 and nums[i+1] == 1:
                counter += 1
            else:
                count.append(counter)
                counter = 1
        count.append(counter)
        return max(count)