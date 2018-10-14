class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[False for i in range(len(grid[i]))] for i in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] == '1':
                    count += 1
                    self.recurssiveVisit(visited, grid, i, j)

        return count

    def recurssiveVisit(self, visited, grid, i, j):
        visited[i][j] = True

        if i + 1 < len(grid) and grid[i + 1][j] == '1' and not visited[i + 1][j]:
            self.recurssiveVisit(visited, grid, i + 1, j)
        if i - 1 >= 0 and grid[i - 1][j] == '1' and not visited[i - 1][j]:
            self.recurssiveVisit(visited, grid, i - 1, j)
        if j + 1 < len(grid[i]) and grid[i][j + 1] == '1' and not visited[i][j + 1]:
            self.recurssiveVisit(visited, grid, i, j + 1)
        if j - 1 >= 0 and grid[i][j - 1] == '1' and not visited[i][j - 1]:
            self.recurssiveVisit(visited, grid, i, j - 1)
