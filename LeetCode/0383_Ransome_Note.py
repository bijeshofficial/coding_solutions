class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_dict = {}
        mag_dict = {}
        for i in ransomNote:
            if i not in ran_dict:
                ran_dict[i] = 1
            else:
                ran_dict[i] += 1
        for i in magazine:
            if i not in mag_dict:
                mag_dict[i] = 1
            else:
                mag_dict[i] += 1
        for k, v in ran_dict.items():
            if k not in mag_dict.keys():
                return False
            else:
                if ran_dict[k] > mag_dict[k]:
                    return False
        return True