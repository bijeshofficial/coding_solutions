class Solution:
    def thousandSeparator(self, n: int) -> str:
        list_of_numbers = list(map(str, str(n)))
        l = []
        counter = 0
        if len(list_of_numbers) > 3:
            for i in reversed(list_of_numbers):
                if counter != 3:
                    l.append(i)
                    counter += 1
                if counter == 3:
                    l.append('.')
                    counter = 0
            if l[-1] == '.':
                return ''.join(l[-2::-1])
            return ''.join(l[::-1])
        return str(n)
