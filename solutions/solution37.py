import copy


def square_index(x, y):
    return x // 3 * 3 + y // 3

class Solution:
    def solve_level_1(self, board, coordinates, row_flags, column_flags, square_flags):
        origin_coordinates = coordinates
        new_coordinates = []
        while len(coordinates) != 0:
            new_coordinates = []
            for x, y in coordinates:
                current_flags = row_flags[x] & column_flags[y] & square_flags[square_index(x, y)]
                if len(current_flags) == 1:
                    for current_flag in current_flags:
                        row_flags[x].remove(current_flag)
                        column_flags[y].remove(current_flag)
                        square_flags[square_index(x, y)].remove(current_flag)
                        board[x][y] = str(current_flag)
                elif len(current_flags) == 0:
                    return False
                else:
                    new_coordinates.append((x, y))
            if len(new_coordinates) == len(coordinates):
                break
            coordinates = new_coordinates
        origin_coordinates.clear()
        for coordinate in new_coordinates:
            origin_coordinates.append(coordinate)
        return True

    def deep_solve(self, origin_board, origin_coordinates, origin_row_flags, origin_column_flags, origin_square_flags):
        x, y = origin_coordinates[-1]
        current_flags = origin_row_flags[x] & origin_column_flags[y] & origin_square_flags[square_index(x, y)]
        for flag in current_flags:
            board = copy.deepcopy(origin_board)
            coordinates = copy.deepcopy(origin_coordinates)
            row_flags = copy.deepcopy(origin_row_flags)
            column_flags = copy.deepcopy(origin_column_flags)
            square_flags = copy.deepcopy(origin_square_flags)
            coordinates.pop()
            board[x][y] = str(flag)
            row_flags[x].remove(flag)
            column_flags[y].remove(flag)
            square_flags[square_index(x, y)].remove(flag)
            is_success = self.solve_level_1(board, coordinates, row_flags, column_flags, square_flags)
            if is_success:
                if len(coordinates) > 0:
                    is_success = self.deep_solve(board, coordinates, row_flags, column_flags, square_flags)
                if is_success:
                    for i in range(9):
                        for j in range(9):
                            origin_board[i][j] = board[i][j]
                    return True
        return False                    

    def solveSudoku(self, board: 'List[List[str]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        row_flags = [set(range(1, 10)) for _ in range(9)]
        column_flags = [set(range(1, 10)) for _ in range(9)]
        square_flags = [set(range(1, 10)) for _ in range(9)]
        coordinates = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    row_flags[i].remove(num)
                    column_flags[j].remove(num)
                    square_flags[square_index(i, j)].remove(num)
                else:
                    coordinates.append((i, j))

        self.solve_level_1(board, coordinates, row_flags, column_flags, square_flags)
        print(board)
        if len(coordinates) > 0:
            self.deep_solve(board, coordinates, row_flags, column_flags, square_flags)
        
        # print(row_flags)
        # print(column_flags)
        # print(square_flags)
        

if __name__ == "__main__":
    # board = [
    #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    # ]
    # print(board)
    # Solution().solveSudoku(board)
    # print(board)


    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    print(board)
    Solution().solveSudoku(board)
    print(board)

