class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x

        low = 1
        high = x
        while low < high:
            mid = low + ((high - low + 1) / 2)
            if x < mid * mid:
                high = mid - 1
            else:
                low = mid

        return low
