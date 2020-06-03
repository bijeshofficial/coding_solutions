class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #This method does not actually do what the question is asking
        #But still produces the correct result
        return sorted(target) == sorted(arr)
    