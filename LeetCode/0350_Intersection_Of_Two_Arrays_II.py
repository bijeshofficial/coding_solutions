class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        emp = []
        if len(nums1) < len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        print(nums1, nums2)
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                emp.append(nums2[i])
                nums1.remove(nums2[i])
            else:
                continue
        return emp