class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = 0
        heights_2 = sorted(heights)
        for i in range(len(heights_2)):
            if heights[i] != heights_2[i]:
                counter +=1
        return counter