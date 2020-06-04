class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        array = []
        arr = sorted(arr)
        difference = max(arr)
        for i in range(len(arr)-1):
            if abs(arr[i] - arr[i+1]) < difference:
                difference  = abs(arr[i] - arr[i+1])
        for i in range(len(arr)-1):
            if abs(arr[i] - arr[i+1]) == difference:
                array.append(arr[i])
                array.append(arr[i+1])
                ans.append(array)
                array = []
        return ans