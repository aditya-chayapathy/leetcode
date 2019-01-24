class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_res = []
        even_res = []
        for item in A:
            if item % 2 == 0:
                even_res.append(item)
            else:
                odd_res.append(item)

        return even_res + odd_res