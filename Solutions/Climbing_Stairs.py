class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n

        sol = [0, 1, 2]
        for i in range(3, n + 1):
            sol.append(sol[i - 1] + sol[i - 2])

        return sol[-1]
