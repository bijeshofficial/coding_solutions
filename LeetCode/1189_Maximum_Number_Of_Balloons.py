class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dictionary = {
            'b':0,
            'a':0,
            'l':0,
            'o':0,
            'n':0
        }
        for i in text:
            if i in dictionary:
                if i == 'o' or i == 'l':
                    dictionary[i] += 0.5
                else:
                    dictionary[i] += 1
            else:
                continue
        return int(min(dictionary.values()))