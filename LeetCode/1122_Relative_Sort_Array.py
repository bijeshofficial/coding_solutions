class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        not_in_ans = []
        j = 0
        for i in arr2:
            for j in range(len(arr1)):
                if arr1[j] == i:
                    ans.append(arr1[j])
        for i in arr1:
            if i not in ans:
                not_in_ans.append(i)

        not_in_ans = sorted(not_in_ans)
        ans += not_in_ans
        return ans