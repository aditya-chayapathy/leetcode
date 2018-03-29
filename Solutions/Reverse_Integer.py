class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = []
        str_x = str(x)
        if str_x[0] == '-':
            result.append('-')
        for i in range(len(str_x) - 1, -1, -1):
            if str_x[i] != '-':
                result.append(str_x[i])

        num = int("".join(result))
        if num < -1 * (2 ** 31) or num > (2 ** 31) - 1:
            return 0

        return num