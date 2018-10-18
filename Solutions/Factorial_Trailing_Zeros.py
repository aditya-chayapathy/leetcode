import math

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        power = 1
        while True:
            quo = n / pow(5, power)
            if quo < 1:
                return count
            count += int(math.floor(quo))
            power += 1
