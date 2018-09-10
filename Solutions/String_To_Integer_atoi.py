class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "":
            return 0

        index = 0
        for i in range(len(str)):
            if str[i] == ' ':
                continue
            else:
                index = i
                break

        if str[index] != "-" and str[index].isalpha():
            return 0

        number = []
        if str[i] in ["+", "-"]:
            number.append(str[i])
            index += 1

        for i in range(index, len(str)):
            if str[i].isnumeric():
                number.append(str[i])
            else:
                break

        if len(number) == 0 or (len(number) == 1 and number[0] in ["-", "+"]):
            return 0

        num = int("".join(number))
        if num > 2 ** 31 - 1:
            num = 2 ** 31 - 1
        if num < -2 ** 31:
            num = -2 ** 31

        return num
