class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_maxima = nums[0]
        global_maxima = nums[0]
        for i in range(1, len(nums)):
            local_maxima = max(nums[i], local_maxima + nums[i])
            global_maxima = max(local_maxima, global_maxima)

        return global_maxima
