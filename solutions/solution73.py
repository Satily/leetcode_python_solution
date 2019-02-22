class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Find 0s
        x_zeros, y_zeros = set(), set()
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == 0:
                    x_zeros.add(x)
                    y_zeros.add(y)
        # Set x Zeros
        for x in x_zeros:
            for y in range(len(matrix[x])):
                matrix[x][y] = 0
        # Set y Zeros
        for x in range(len(matrix)):
            for y in y_zeros:
                matrix[x][y] = 0


if __name__ == "__main__":
    matrices = [
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ],
    ]
    for matrix in matrices:
        Solution().setZeroes(matrix)
        print(matrix)
