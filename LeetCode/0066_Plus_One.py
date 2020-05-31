class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_list = [str(x) for x in digits]
        added_int = int(''.join(str_list))+1
        main_list = [int(x) for x in str(added_int)]
        return main_list