from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_dict = Counter(s)
        for i in range(len(s)):
            if count_dict[s[i]] == 1:
                return i

        return -1
