class Solution:
    def validTicTacToe(self, board: 'List[str]') -> bool:
        x_count, o_count = 0, 0
        for row in board:
            for grid in row:
                if grid == 'X':
                    x_count += 1
                elif grid == 'O':
                    o_count += 1
        if x_count < o_count or x_count > o_count + 1:
            return False
        v_count = 0
        for index in range(3):
            if board[index][0] == board[index][1] == board[index][2]:
                v_count += 1
            if board[0][index] == board[1][index] == board[2][index]:
                v_count += 1
        if board[0][0] == board[1][1] == board[2][2]:
            v_count += 1
        if board[0][2] == board[1][1] == board[2][0]:
            v_count += 1
        return v_count <= 1


if __name__ == "__main__":
    print(Solution().validTicTacToe(["O  ", "   ", "   "]))
    print(Solution().validTicTacToe(["XOX", " X ", "   "]))
    print(Solution().validTicTacToe(["XXX", "   ", "OOO"]))
    print(Solution().validTicTacToe(["XOX", "O O", "XOX"]))
