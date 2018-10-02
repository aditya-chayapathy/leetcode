class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        res = s[0]
        for i in range(len(s) - 1):
            temp1 = self.palindromicSubstring(s, i, i)
            temp2 = self.palindromicSubstring(s, i, i + 1)
            if len(temp1) > len(res):
                res = temp1
            if len(temp2) > len(res):
                res = temp2

        return res

    def palindromicSubstring(self, str, i, j):
        while i >= 0 and j < len(str) and str[i] == str[j]:
            i -= 1
            j += 1

        return str[i + 1:j]
