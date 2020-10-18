class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        remove = int(len(arr) * 0.05)
        new_list = arr[remove:len(arr)-remove]
        return sum(new_list)/len(new_list)
