class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 0
        j = 0
        window = set()
        while (i < len(s) and j < len(s)):
            if s[j] not in window:
                window.add(s[j])
                j += 1
                result = max(result, len(window))
            else:
                window.remove(s[i])
                i += 1

        return result