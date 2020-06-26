class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) > 1:
                return i

'''This has a runtime of O(n**2).
This does not satisfy the rumtime complexity
So better would be to use two pointer approach
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.'''