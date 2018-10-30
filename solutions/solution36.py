class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        l = 9
        # check rows
        for i in range(0, l):
            flag_set = set()
            for j in range(0, l):
                if board[i][j] != '.':
                    if board[i][j] in flag_set:
                        return False
                    flag_set.add(board[i][j])
        # check columns
        for i in range(0, l):
            flag_set = set()
            for j in range(0, l):
                if board[j][i] != '.':
                    if board[j][i] in flag_set:
                        return False
                    flag_set.add(board[j][i])
        # check sub-boxes
        for x in range(0, 3):
            for y in range(0, 3):
                flag_set = set()
                for i in range(0, 3):
                    for j in range(0, 3):
                        rx, ry = x * 3 + i, y * 3 + j
                        if board[rx][ry] != '.':
                            if board[rx][ry] in flag_set:
                                return False
                            flag_set.add(board[rx][ry])
        return True


if __name__ == "__main__":
    print(Solution().isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
    ))
    print(Solution().isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
    ))