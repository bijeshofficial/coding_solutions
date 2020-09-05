class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dictionary = {}
        answer = ''
        for i in range(len(s)):
            dictionary[indices[i]] = s[i]
        for k in sorted(dictionary):
            answer += dictionary[k]
        return answer
