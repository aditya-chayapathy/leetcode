class Solution(object):
    def isHappy(self, n):
        already_explored = []
        str_num = str(n)
        while str_num not in already_explored:
            already_explored.append(str_num)
            sum = 0
            for digit in str_num:
                sum += int(digit) ** 2
            if sum == 1:
                return True
            str_num = str(sum)

        return False
