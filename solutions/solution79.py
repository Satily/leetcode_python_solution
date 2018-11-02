class Solution:
    def __init__(self):
        self.directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

    def dfs(self, board, word, board_flag, cord, deep, lw, lm, ln):
        if deep == lw:
            return True
        for d in self.directions:
            n_cord = (cord[0] + d[0], cord[1] + d[1])
            if 0 <= n_cord[0] < lm and 0 <= n_cord[1] < ln and not board_flag[n_cord[0]][n_cord[1]] and board[n_cord[0]][n_cord[1]] == word[deep]:
                board_flag[n_cord[0]][n_cord[1]] = True
                if self.dfs(board, word, board_flag, n_cord, deep + 1, lw, lm, ln):
                    return True
                board_flag[n_cord[0]][n_cord[1]] = False
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Consts

        lw = len(word)
        lm = len(board)
        if lw == 0:
            return True
        if lm <= 0:
            return False
        ln = len(board[0])
        if ln <= 0:
            return False
        # Begin
        board_flag = [[False] * ln for _ in range(0, lm)]
        for x, line in enumerate(board):
            for y, ele in enumerate(line):
                if ele == word[0]:
                    board_flag[x][y] = True
                    if self.dfs(board, word, board_flag, (x, y), 1, lw, lm, ln):
                        return True
                    board_flag[x][y] = False
        return False


if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(Solution().exist(board, 'ABCCED'))
    print(Solution().exist(board, 'SEE'))
    print(Solution().exist(board, 'ABCB'))
