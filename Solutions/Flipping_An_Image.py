class Solution(object):
    def flip(self, num):
        if num == 1:
            return 0
        else:
            return 1

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(len(A)):
            temp = []
            for j in range(len(A[i])):
                temp.append(self.flip(A[i][len(A[i]) - 1 - j]))
            result.append(temp)

        return result