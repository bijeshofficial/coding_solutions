class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = sorted(nums1+nums2)
        if len(new_list) == 1:
            return new_list[0]
        if len(new_list) % 2 == 0:
            return (new_list[len(new_list)//2] + new_list[(len(new_list)//2) - 1]) / 2
        else:
            return (new_list[len(new_list)//2])