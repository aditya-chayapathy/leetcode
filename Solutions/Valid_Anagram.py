from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counter = Counter(s)
        t_counter = Counter(t)
        if len(s_counter.keys()) != len(t_counter.keys()):
            return False
        if len(set(s_counter.keys()) - set(t_counter.keys())) != 0:
            return False

        for s_item in s_counter.keys():
            if s_counter[s_item] != t_counter[s_item]:
                return False

        return True
