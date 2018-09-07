class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp1 = nums[-k:]
        temp2 = nums[:-k]
        for i in range(len(temp1)):
            nums[i] = temp1[i]
        for i in range(len(temp1), len(temp2) + len(temp1)):
            nums[i] = temp2[i - len(temp1)]
        print(nums)
