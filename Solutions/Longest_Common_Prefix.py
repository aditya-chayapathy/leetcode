class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        index = 0
        min_length = float("+inf")
        for i in range(len(strs)):
            if len(strs[i]) <= min_length:
                index = i
                min_length = len(strs[i])

        res = []
        for i in range(min_length):
            char = strs[index][i]
            present_in_all = False
            for j in range(len(strs)):
                if strs[j][i] != char:
                    break
                if j == len(strs) - 1:
                    present_in_all = True
            if present_in_all:
                res.append(char)
            else:
                break

        return "".join(res)