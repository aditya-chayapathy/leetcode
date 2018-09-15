class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        for item in sorted(nums):
            if item != count:
                return count
            else:
                count += 1

        return count
