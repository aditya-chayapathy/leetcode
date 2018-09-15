# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(n) == True and isBadVersion(n - 1) == False:
            return n

        if isBadVersion(1) == True:
            return 1

        start = 0
        end = n
        while True:
            x = int((end - start) / 2 + start)
            prev = isBadVersion(x - 1)
            curr = isBadVersion(x)
            if prev == False and curr == True:
                return int(x)
            elif prev == False and curr == False:
                start = int(x)
            elif prev == True and curr == True:
                end = int(x)
