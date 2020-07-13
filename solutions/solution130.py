class Solution:
    def solve(self, board: 'List[List[str]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]

        def dfs(x, y, board, m, n):
            flag = True
            board[x][y] = 'C'
            for delta_x, delta_y in directions:
                new_x, new_y = x + delta_x, y + delta_y
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'O':
                    dfs(new_x, new_y, board, m, n)
            return flag

        m = len(board)
        for x in range(m):
            n = len(board[x])
            if board[x][0] == 'O':
                dfs(x, 0, board, m, n)
            if board[x][n - 1] == 'O':
                dfs(x, n - 1, board, m, n)
        if m > 0:
            n = len(board[0])
            for y in range(n):
                if board[0][y] == 'O':
                    dfs(0, y, board, m, n)
                if board[m - 1][y] == 'O':
                    dfs(m - 1, y, board, m, n)

        for x in range(m):
            n = len(board[x])
            for y in range(n):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'C':
                    board[x][y] = 'O'


if __name__ == "__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    Solution().solve(board)
    print(board)

    board = [
        ["O", "O", "O", "O", "X", "X"],
        ["O", "O", "O", "O", "O", "O"],
        ["O", "X", "O", "X", "O", "O"],
        ["O", "X", "O", "O", "X", "O"],
        ["O", "X", "O", "X", "O", "O"],
        ["O", "X", "O", "O", "O", "O"]
    ]
    Solution().solve(board)
    print(board)
