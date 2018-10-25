class Solution:
    def rotateMatrix(self, A):
        if len(A) % 2 == 0:
            num_layers = int(len(A) / 2)
        else:
            num_layers = int((len(A) + 1) / 2)

        for layer in range(num_layers):
            top = layer
            bottom = len(A) - layer - 1
            for item in range(top, bottom):
                temp = A[top][item]
                A[top][item] = A[bottom - item + top][top]
                A[bottom - item + top][top] = A[bottom][bottom - item + top]
                A[bottom][bottom - item + top] = A[item][bottom]
                A[item][bottom] = temp

        return A

