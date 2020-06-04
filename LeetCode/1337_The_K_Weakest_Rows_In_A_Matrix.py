class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count_one = 0
        list_1 = []
        ans = []
        for i in mat:
            for j in i:
                if j == 1:
                    count_one += 1
            list_1.append(count_one)
            count_one = 0
        for i in range(k):
            ans.append(list_1.index(min(list_1)))
            list_1[list_1.index(min(list_1))] = max(list_1) + 1
        print(list_1)
        return ans