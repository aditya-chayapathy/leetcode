class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [s[0]]
        for i in range(1, len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif stack[len(stack) - 1] == '[' and s[i] == ']' or stack[len(stack) - 1] == '(' and s[i] == ')' or stack[
                len(stack) - 1] == '{' and s[i] == '}':
                stack.pop()
            else:
                stack.append(s[i])

        if len(stack) > 0:
            return False
        else:
            return True