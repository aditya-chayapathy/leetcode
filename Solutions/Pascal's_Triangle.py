class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [
                [1],
                [1, 1]
            ]

        res = [
            [1],
            [1, 1]
        ]
        for i in range(numRows - 2):
            temp = [1 for _ in range(i + 3)]
            for j in range(len(temp)):
                if j not in [0, len(temp) - 1]:
                    temp[j] = res[1 + i][j] + res[1 + i][j - 1]
            res.append(temp)

        return res
