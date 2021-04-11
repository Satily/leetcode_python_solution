class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        if len(grid) == 0:
            return 0
        else:
            return grid[-1][-1]


if __name__ == "__main__":
    print(Solution().minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
