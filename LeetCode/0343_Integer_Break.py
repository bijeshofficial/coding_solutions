class Solution:
    def integerBreak(self, n: int) -> int:
        pieces_of_three = 0
        pieces_of_two = 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        pieces_of_three += n // 3
        if n % 3 == 1:
            pieces_of_two += 2
            if pieces_of_three > 0:
                pieces_of_three -= 1
        if n % 3 == 2:
            pieces_of_two += 1
        return (3**pieces_of_three) * (2**pieces_of_two)
