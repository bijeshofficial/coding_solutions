class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = 0
        empty_list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j] and nums[i] != nums[j]:
                    counter +=1
            empty_list.append(counter)
            counter = 0
        return empty_list