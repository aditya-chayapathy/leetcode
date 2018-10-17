class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ["+", "-", "*", "/"]:
                exp2 = stack.pop()
                exp1 = stack.pop()
                if tokens[i] == "+":
                    res = exp1 + exp2
                elif tokens[i] == "-":
                    res = exp1 - exp2
                elif tokens[i] == "*":
                    res = exp1 * exp2
                else:
                    if exp1 * exp2 < 0 and exp1 % exp2 != 0:
                        res = exp1 / exp2 + 1
                    else:
                        res = exp1 / exp2
                stack.append(res)
            else:
                stack.append(int(tokens[i]))

        return stack.pop()
