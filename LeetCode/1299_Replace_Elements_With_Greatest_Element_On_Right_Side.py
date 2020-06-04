class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        empty_list = []
        for i in range(len(arr)):
            empty_list.append(max(arr[i:]))
        empty_list.pop(0)
        empty_list.append(-1)
        return empty_list