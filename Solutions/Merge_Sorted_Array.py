class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i - m]

        pos = 0
        for item in sorted(nums1):
            nums1[pos] = item
            pos += 1
