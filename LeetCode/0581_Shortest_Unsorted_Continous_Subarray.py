class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a = sorted(nums)
        list_1 = []
        for i in range(len(nums)):
            if nums[i] != a[i]:
                list_1.append(i)
        # print(list_1)
        if list_1:
            return max(list_1)-min(list_1) + 1
        return 0