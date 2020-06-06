class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
            while(len(stones) != 1):
                a = stones.pop(stones.index(max(stones)))
                b = stones.pop(stones.index(max(stones)))
                stones.append(a-b)
            return stones[0]