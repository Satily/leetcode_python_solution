class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in range(rowIndex):
            for j in reversed(range(1, len(result))):
                result[j] += result[j - 1]
            result.append(1)
        return result


if __name__ == "__main__":
    print(Solution().getRow(0))
    print(Solution().getRow(1))
    print(Solution().getRow(2))
    print(Solution().getRow(3))
    print(Solution().getRow(4))
    print(Solution().getRow(5))
    print(Solution().getRow(6))
