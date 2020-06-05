class Solution:
    def removeDuplicates(self, S: str) -> str:
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                return self.removeDuplicates(S[:i]+S[i+2:])
        return S