class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = f'{x:b}'
        bin_y = f'{y:b}'
        counter = 0
        max_length = len(max(bin_x,bin_y,key=len))
        if len(bin_x) != max_length:
            bin_x = bin_x.zfill(max_length)
        elif len(bin_y) != max_length:
            bin_y = bin_y.zfill(max_length)
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                counter += 1
        return counter