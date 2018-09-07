class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp_dict = {}
        for item in nums:
            if item in temp_dict.keys():
                return True
            else:
                temp_dict[item] = 1

        return False
