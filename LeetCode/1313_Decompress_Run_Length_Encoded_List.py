class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        empty_list = []
        for i in range(0,len(nums)-1,2):
            freq = nums[i]
            val = nums[i+1]
            for i in range(freq):
                empty_list.append(val)
        return empty_list