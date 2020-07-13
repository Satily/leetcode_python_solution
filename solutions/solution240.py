class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        x, y = m - 1, 0
        while matrix[x][y] != target:
            if matrix[x][y] < target and y < n - 1:
                y += 1
            elif matrix[x][y] > target and x > 0:
                x -= 1
            else:
                break
        return matrix[x][y] == target


if __name__ == "__main__":
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(Solution().searchMatrix(matrix, 5))
    print(Solution().searchMatrix(matrix, 20))
