class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set(nums)
        b = set(x for x in range(1,len(nums)+1))
        return list(b.difference(a))