class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(1, numRows):
            line = [1]
            for j in range(1, i):
                line.append(result[-1][j - 1] + result[-1][j])
            line.append(1)
            result.append(line)
        return result


if __name__ == "__main__":
    print(Solution().generate(5))
    print(Solution().generate(0))
    print(Solution().generate(1))

