class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        res = [nums[0]]
        res.append(max(res[0], nums[1]))
        for i in range(2, len(nums)):
            res.append(max(nums[i] + res[i - 2], res[i - 1]))

        return res[-1]
