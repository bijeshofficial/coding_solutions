class Solution:
    def maximum69Number (self, num: int) -> int:
        list_1 = [int(x) for x in str(num)]
        for i in range(len(list_1)):
            if list_1[i] == 6:
                list_1[i] = 9
                break
        return int(''.join(str(x) for x in list_1))