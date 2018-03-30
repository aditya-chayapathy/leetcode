class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for item in nums:
            if item == val:
                count += 1

        for i in range(count):
            nums.remove(val)

        return len(nums)