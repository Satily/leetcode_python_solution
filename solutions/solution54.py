class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        flag_matrix = [[False] * n for x in range(m)]
        x, y, d_index = 0, 0, 0
        flag_matrix[0][0] = True
        result = [matrix[0][0]]
        for _ in range(m * n - 1):
            nx, ny = x + directions[d_index % 4][0], y + directions[d_index % 4][1]
            if 0 <= nx < m and 0 <= ny < n and not flag_matrix[nx][ny]:
                x, y = nx, ny
            else:
                d_index += 1
                x, y = x + directions[d_index % 4][0], y + directions[d_index % 4][1]
            flag_matrix[x][y] = True
            result.append(matrix[x][y])
        return result


if __name__ == "__main__":
    print(Solution().spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
    print(Solution().spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]))
