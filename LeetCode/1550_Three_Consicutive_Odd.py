class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                counter += 1
            elif arr[i] % 2 == 0:
                counter = 0
            if counter == 3:
                return True
        return False
