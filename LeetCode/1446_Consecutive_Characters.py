class Solution:
    def maxPower(self, s: str) -> int:
        main_counter = 1
        counter_2 = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                counter_2 += 1
            if counter_2 > main_counter:
                main_counter = counter_2
            elif s[i] != s[i+1]:
                counter_2 = 1
        return main_counter