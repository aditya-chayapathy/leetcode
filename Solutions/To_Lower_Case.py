class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for char in str:
            if char.isupper():
                res += chr(ord(char) + 32)
            else:
                res += char

        return res