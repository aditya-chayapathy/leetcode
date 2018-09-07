class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                intersection.append(nums1[i])
                del nums2[nums2.index(nums1[i])]

        return intersection
