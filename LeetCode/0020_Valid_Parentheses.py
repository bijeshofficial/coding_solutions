class Solution:
    def isValid(self, s: str) -> bool:
        dictionary_of_braces = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
        empty_list = []
        for i in s:
            if i in dictionary_of_braces.keys():
                empty_list.append(i)
            elif len(empty_list) == 0 or dictionary_of_braces[empty_list.pop()] != i:
                return False
        return empty_list == []