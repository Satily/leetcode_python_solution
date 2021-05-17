class NumMatrix:
    def __init__(self, matrix: 'List[List[int]]'):
        height = len(matrix)
        width = 0 if height == 0 else len(matrix[0])
        self.sums = [[0] * (width + 1) for _ in range(height + 1)]
        for i in range(1, height + 1):
            s = 0
            for j in range(1, width + 1):
                s += matrix[i - 1][j - 1]
                self.sums[i][j] = self.sums[i - 1][j] + s

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2 + 1][col2 + 1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1] + self.sums[row1][col1]


if __name__ == '__main__':
    num_matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(num_matrix.sumRegion(2, 1, 4, 3))
    print(num_matrix.sumRegion(1, 1, 2, 2))
    print(num_matrix.sumRegion(1, 2, 2, 4))

