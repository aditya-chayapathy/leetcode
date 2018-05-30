class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row_dict = {}
        index_arr = []
        for index in range(numRows):
            index_arr.append(index)
            row_dict[index] = []
            
        for index in range(numRows-2, 0, -1):
            index_arr.append(index)
        
        pos = 0
        for index in range(len(s)):
            row_dict[index_arr[pos]].append(s[index])
            pos += 1
            if pos == len(index_arr):
                pos = 0
        
        result = []
        for index in range(numRows):
            result = result + row_dict[index]
        
        return "".join(result)
