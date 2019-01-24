class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count_dict = {}
        for item in A:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1

            if count_dict[item] == len(A) / 2:
                return item
