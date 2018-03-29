class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) in [0, 1]:
            return len(nums)

        i = 0
        j = 1
        while True:
            if j == len(nums):
                break
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]

        for k in range(len(nums) - 1, i, -1):
            del nums[k]

        return len(nums)