class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_list = nums[:n]
        second_list = nums[n:]
        emp = []
        for i in range(n):
            emp.append(first_list[i])
            emp.append(second_list[i])
        return emp