import numpy as np

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        input_arr = np.array(grid)
        for row_index in range(len(input_arr)):
            for column_index in range(len(input_arr[row_index])):
                result += min(max(input_arr[:, column_index]), max(input_arr[row_index, :])) - input_arr[row_index][column_index]
                
        return int(result)
