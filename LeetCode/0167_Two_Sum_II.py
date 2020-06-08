class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictionary = {}
        for i ,v in enumerate(numbers):
            remaining = target - v
            if remaining in dictionary:
                return [dictionary[remaining]+1,i+1]
            dictionary[v] = i
        return []