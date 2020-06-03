class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        k = 0
        while k < len(nums):
            if nums[k] == 0:
                nums.pop(k)
                counter +=1
                k -=1
            k +=1
        for i in range(counter):
            nums.append(0)