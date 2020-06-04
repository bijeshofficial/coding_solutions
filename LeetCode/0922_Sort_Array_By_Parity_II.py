class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even_list = [x for x in A if x%2 == 0]
        odd_list = [x for x in A if x%2 !=0]
        ans = []
        for i in range(len(A)//2):
            ans.append(even_list[i])
            ans.append(odd_list[i])
        return ans