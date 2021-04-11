class Solution:
    def numTrees(self, n: 'int') -> 'int':
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
            dp[i][1] = 1
        for l in range(2, n + 1):
            for i in range(n + 1 - l):
                for left in range(l):
                    dp[i][l] += dp[i][left] * dp[i + left + 1][l - left - 1]
        return dp[0][n]


if __name__ == "__main__":
    print(Solution().numTrees(3))
