class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        list_1 = []
        candies_to_give = 1
        i = 0
        for j in range(num_people):
            list_1.append(0)
        while candies > 0:
            if candies> candies_to_give:
                list_1[i] += candies_to_give
            else:
                list_1[i] += candies
            if i != num_people-1:
                i += 1
            else:
                i = 0
            candies -= candies_to_give
            candies_to_give += 1
        return list_1