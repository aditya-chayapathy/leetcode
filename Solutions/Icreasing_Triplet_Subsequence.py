class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        min1 = float("inf")
        min2 = float("inf")
        for i in range(len(nums)):
            if nums[i] <= min1:
                min1 = nums[i]
            elif nums[i] <= min2:
                min2 = nums[i]
            else:
                return True

        return False
