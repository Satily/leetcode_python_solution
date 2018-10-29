class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ls = len(s)
        # First Line
        result_list_item = []
        step = (numRows - 1) * 2
        for i in range(0, ls, step):
            result_list_item.append(s[i])
        result_list = [result_list_item]
        # Middle Lines
        for line_index in range(1, numRows - 1):
            result_list_item1 = []
            result_list_item2 = []
            for i in range(line_index, ls, step):
                result_list_item1.append(s[i])
            for i in range(step - line_index, ls, step):
                result_list_item2.append(s[i])
            result_list_item = []
            for i in range(0, max(len(result_list_item1), len(result_list_item2))):
                if i < len(result_list_item1):
                    result_list_item.append(result_list_item1[i])
                if i < len(result_list_item2):
                    result_list_item.append(result_list_item2[i])
            result_list.append(result_list_item)
        # Last Line
        result_list_item = []
        for i in range(numRows - 1, ls, step):
            result_list_item.append(s[i])
        result_list.append(result_list_item)
        return ''.join([''.join(result_list_item) for result_list_item in result_list])


if __name__ == "__main__":
    print(Solution().convert('PAYPALISHIRING', 3))
    print(Solution().convert('PAYPALISHIRING', 4))
    print(Solution().convert('PAYPALISHIRING', 1))
