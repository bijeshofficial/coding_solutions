class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        list_1 = []
        counter = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                counter += 1
                list_1.append(counter)
            else:
                counter = 1
        if len(nums) == 1:
            return counter
        elif len(nums) < 1:
            return 0
        if list_1:
            return max(list_1)
        return counter