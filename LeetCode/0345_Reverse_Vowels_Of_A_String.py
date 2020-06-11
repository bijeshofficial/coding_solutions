class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        vowel = ''
        ans = ''
        for i in s:
            if i in vowels:
                vowel += i
        vowel_to_add = vowel[::-1]
        j = 0
        for i in s:
            if i not in vowels:
                ans += i
            else:
                ans += vowel_to_add[j]
                j += 1
        return ans