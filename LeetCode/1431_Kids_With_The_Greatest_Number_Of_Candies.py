class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_of_list = max(candies)
        empty_list = []
        for i in candies:
            if i + extraCandies >= max_of_list:
                empty_list.append(True)
            else:
                empty_list.append(False)
        return empty_list