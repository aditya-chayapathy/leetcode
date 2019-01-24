class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        A = [item for item in range(len(S) + 1)]
        res = []

        for item in S:
            if item == "I":
                res.append(A[0])
                del A[0]
            else:
                res.append(A[len(A) - 1])
                del A[len(A) - 1]

        res.append(A[0])

        return res