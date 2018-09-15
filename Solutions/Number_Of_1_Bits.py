class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_n = "{0:b}".format(n)
        count = 0
        for item in bin_n:
            if item == '1':
                count += 1

        return count
