class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        dictionary = {}
        list_1 = []
        for i in A:
            for j in A[0]:
                if j not in dictionary:
                    dictionary[j] = 1
                else:
                    dictionary[j] += 1

        for i in A:
            for j in dictionary.keys():
                if i.count(j) < dictionary[j]:
                    dictionary[j] = i.count(j)

        for k ,v in dictionary.items():
            for i in range(v):
                list_1.append(k)

        return list_1