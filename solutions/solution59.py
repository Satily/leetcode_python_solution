class Solution:
    def generateMatrix(self, n: int) -> 'List[List[int]]':
        acc = 1
        result = [[0] * n for _ in range(n)]
        half = n // 2
        for i in range(half):
            for j in range(i, n - 1 - i):
                result[i][j] = acc
                acc += 1
            for j in range(i, n - 1 - i):
                result[j][n - 1 - i] = acc
                acc += 1
            for j in range(i, n - 1 - i):
                result[n - 1 - i][n - 1 - j] = acc
                acc += 1
            for j in range(i, n - 1 - i):
                result[n - 1 - j][i] = acc
                acc += 1
        if n & 1 == 1:
            result[n // 2][n // 2] = acc
        return result


def print_matrix(matrix):
    print('[')
    for i in range(len(matrix)):
        print(matrix[i])
    print(']')


if __name__ == '__main__':
    print_matrix(Solution().generateMatrix(3))
    print_matrix(Solution().generateMatrix(4))
    print_matrix(Solution().generateMatrix(5))
    print_matrix(Solution().generateMatrix(6))
