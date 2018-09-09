class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) in [0, 1]:
            return True

        s = ''.join([char.lower() for char in filter(str.isalnum, s)])
        reversed_s = ''.join(reversed(list(s)))
        if s == reversed_s:
            return True
        else:
            return False
