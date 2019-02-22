class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        directions = [
            [-1, 0],
            [-1, 1],
            [0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
            [-1, -1],
        ]

        def dfs(board, m, n, x, y):
            coors = []
            for direction in directions:
                nx, ny = x + direction[0], y + direction[1]
                if 0 <= nx < m and 0 <= ny < n:
                    coors.append((nx, ny))
            s = 0
            for nx, ny in coors:
                if board[nx][ny] in {'X', 'M'}:
                    s += 1
            if s == 0:
                board[x][y] = "B"
                for nx, ny in coors:
                    if board[nx][ny] == 'E':
                        dfs(board, m, n, nx, ny)
            else:
                board[x][y] = str(s)

        x, y = click[0], click[1]
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            m, n = len(board), len(board[0])
            if board[x][y] == "E":
                dfs(board, m, n, x, y)
            elif board[x][y] == "M":
                board[x][y] = "X"

        return board


if __name__ == "__main__":
    print(Solution().updateBoard([
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'M', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E']
    ], [3, 0]))
    print(Solution().updateBoard([
        ['B', '1', 'E', '1', 'B'],
        ['B', '1', 'M', '1', 'B'],
        ['B', '1', '1', '1', 'B'],
        ['B', 'B', 'B', 'B', 'B']
    ], [1, 2]))
