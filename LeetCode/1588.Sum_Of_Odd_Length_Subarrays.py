class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        step, ans = 1, 0
        while step < len(arr) + 1:
            for i in range(0, len(arr)):
                if len(arr[i:i + step]) == step:
                    ans += sum(arr[i:i + step])
                    continue
                break
            step += 2
        return ans
