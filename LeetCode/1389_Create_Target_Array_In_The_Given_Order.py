class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output_list = []
        for i in range(len(nums)):
            output_list.insert(index[i],nums[i])
        return output_list