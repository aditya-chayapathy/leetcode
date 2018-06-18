class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        index = self.recurssiveSolution(A)

        return index

    def recurssiveSolution(self, A):
        size = len(A)
        left_half = A[:int(size / 2)]
        middle = A[int(size / 2)]
        right_half = A[int(size / 2) + 1:]

        if len(right_half) == 0:
            right_half = [-1]
        if len(left_half) == 0:
            left_half = [-1]

        if left_half[-1] <= middle <= right_half[0]:
            return len(left_half) + 1 + self.recurssiveSolution(right_half)
        elif left_half[-1] >= middle >= right_half[0]:
            return self.recurssiveSolution(left_half)
        elif left_half[-1] <= middle >= right_half[0]:
            return int(size / 2)