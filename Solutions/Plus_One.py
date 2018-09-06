class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(list(set(digits))) == 1 and list(set(digits))[0] == 9:
            return [1] + list([0 for i in range(len(digits))])

        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        i = 1
        while True:
            if digits[-i] != 9:
                digits[-i] += 1
                break
            else:
                digits[-i] = 0
                i += 1

        return digits
