class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        min_point = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_point:
                min_point = prices[i]
            elif prices[i] - min_point > max_profit:
                max_profit = prices[i] - min_point

        return max_profit
