class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        local_maxima = 0
        global_maxima = 0
        for i in range(1, len(prices)):
            local_maxima = max(0, local_maxima + (prices[i] - prices[i - 1]))
            global_maxima = max(global_maxima, local_maxima)

        return global_maxima
