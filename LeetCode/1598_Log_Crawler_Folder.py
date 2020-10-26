class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for l in logs:
            if l == '../' and cnt:
                cnt -= 1
            elif l != './' and l != '../':
                cnt += 1
        return cnt
