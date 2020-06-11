class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_1 = [x/2 for x in arr]
        for i in range(len(arr_1)):
            if arr_1[i] == arr[i]:
                arr.pop(i)
                break
        for i in arr_1:
            if i in arr:
                return True
        return False