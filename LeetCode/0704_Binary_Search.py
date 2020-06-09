class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_index = 0
        last_index = len(nums) - 1
        while first_index<last_index:
            middle = (first_index+last_index) // 2
            if (nums[middle]< target):
                first_index = middle + 1
            else:
                last_index = middle
        if nums[first_index] == target:
            return first_index
        return -1