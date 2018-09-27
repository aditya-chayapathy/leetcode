class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = []
        columns = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)

        for row in rows:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0

        for column in columns:
            for i in range(len(matrix)):
                matrix[i][column] = 0
