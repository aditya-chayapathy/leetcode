class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float("+inf")
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.min = min(self.stack)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        if len(self.stack) > 0:
            self.min = min(self.stack)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
