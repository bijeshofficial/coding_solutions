class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        while len(points)>1:
            a = points.pop(0)
            b = points[0]
            distance += max(abs(a[0]-b[0]),abs(a[1]-b[1]))
        return distance