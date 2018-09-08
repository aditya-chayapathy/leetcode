class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            visited = {}
            for j in range(len(board)):
                if board[i][j] in visited.keys() and board[i][j] != ".":
                    return False
                visited[board[i][j]] = 1

        for i in range(len(board)):
            visited = {}
            for j in range(len(board)):
                if board[j][i] in visited.keys() and board[j][i] != ".":
                    return False
                visited[board[j][i]] = 1

        for left in range(0, len(board), 3):
            right = left + 2
            for top in range(0, len(board), 3):
                bottom = top + 2
                visited = {}
                for i in range(left, right + 1):
                    for j in range(top, bottom + 1):
                        if board[i][j] in visited.keys() and board[i][j] != ".":
                            return False
                        visited[board[i][j]] = 1

        return True
