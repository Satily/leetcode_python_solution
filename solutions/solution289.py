from itertools import product


class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def is_inside(_x, _y):
            return 0 <= _x < len(board) and 0 <= _y < len(board[0])
        directions = list(filter(lambda x: x != (0, 0), product(list(range(-1, 2, 1)), list(range(-1, 2, 1)))))
        if len(board) == 0 or len(board[0]) == 0:
            return
        for x in range(len(board)):
            for y in range(len(board[x])):
                alive_neighbors = 0
                for d in directions:
                    nx, ny = x + d[0], y + d[1]
                    if is_inside(nx, ny):
                        alive_neighbors += board[nx][ny] & 1
                if board[x][y] == 1:
                    if 2 <= alive_neighbors <= 3:
                        board[x][y] += board[x][y] << 1
                elif alive_neighbors == 3:
                    board[x][y] += 2
        for x in range(len(board)):
            for y in range(len(board[x])):
                board[x][y] >>= 1


if __name__ == "__main__":
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    Solution().gameOfLife(board)
    print(board)
