class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = "{0:b}".format(x)
        bin_y = "{0:b}".format(y)
        if len(bin_x) != len(bin_y):
            if len(bin_x) > len(bin_y):
                smaller = "y"
            else:
                smaller = "x"
            if smaller == "x":
                diff = len(bin_y) - len(bin_x)
                temp = diff * '0'
                bin_x = temp + bin_x
            else:
                diff = len(bin_x) - len(bin_y)
                temp = diff * '0'
                bin_y = temp + bin_y

        count = 0
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                count += 1

        return count
