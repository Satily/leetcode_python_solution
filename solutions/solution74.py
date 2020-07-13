class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        left, right = 0, m * n
        while left + 1 < right:
            mid = (left + right) >> 1
            num = matrix[mid // n][mid % n]
            if num < target:
                left = mid
            elif num > target:
                right = mid
            else:
                return True
        return matrix[left // n][left % n] == target


if __name__ == "__main__":
    # matrix = [
    #     [1, 3, 5, 7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 50]
    # ]
    # target = 3
    # print(Solution().searchMatrix(matrix, target))
    #
    # matrix = [
    #     [1, 3, 5, 7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 50]
    # ]
    # target = 13
    # print(Solution().searchMatrix(matrix, target))

    matrix = [[]]
    target = 1
    print(Solution().searchMatrix(matrix, target))
