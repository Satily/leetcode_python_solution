class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m <= 0:
            return 0
        n = len(obstacleGrid[0])
        if n <= 0 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(0, m)]
        dp[0][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 0:
                    if i != 0 and obstacleGrid[i - 1][j] == 0:
                        dp[i][j] += dp[i - 1][j]
                    if j != 0 and obstacleGrid[i][j - 1] == 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles(
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    ))
