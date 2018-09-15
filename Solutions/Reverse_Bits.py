class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_n = "{0:b}".format(n)
        if len(bin_n) != 32:
            diff = 32 - len(bin_n)
            temp = diff * '0'
            bin_n = temp + bin_n
        rev_bin_n = "".join(list(reversed(list(bin_n))))
        rev_int_n = int(rev_bin_n, 2)

        return rev_int_n
