class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) in [0, 1]:
            return 0

        start = -1
        profit = 0
        searchingForStart = True
        for i in range(len(prices) - 1):
            if searchingForStart:
                if prices[i] < prices[i + 1]:
                    start = i
                    searchingForStart = False
                    continue
            else:
                if prices[i] > prices[i + 1]:
                    end = i
                    searchingForStart = True
                    profit += (prices[end] - prices[start])

        if prices[-1] >= prices[-2]:
            end = len(prices) - 1
            profit += (prices[end] - prices[start])

        return profit
