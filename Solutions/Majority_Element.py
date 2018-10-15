class Solution(object):
    def majorityElement(self, nums):

        hash_map = {}
        for item in nums:
            if item in hash_map.keys():
                hash_map[item] += 1
            else:
                hash_map[item] = 1

            if hash_map[item] > len(nums) / 2:
                return item
