class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        for i in range((m + 1) // 2):
            for j in range(m // 2):
                matrix[i][j], matrix[j][m - 1 - i], matrix[m - 1 - i][m - 1 - j], matrix[m - 1 - j][i] = matrix[m - 1 - j][i], matrix[i][j], matrix[j][m - 1 - i], matrix[m - 1 - i][m - 1 - j]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Solution().rotate(matrix)
    print(matrix)
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    Solution().rotate(matrix)
    print(matrix)

