class Solution:
    def findTargetSumWays(self, nums: 'List[int]', S: 'int') -> 'int':
        if not (-1000 <= S <= 1000):
            return 0
        dp = [[0] * 2001 for _ in range(2)]
        dp[0][1000] = 1
        c, n = 1, 0
        for num in nums:
            c, n = n, c
            dp[n] = [0] * 2001
            for i in range(len(dp[c])):
                if dp[c][i] > 0:
                    dp[n][i + num] += dp[c][i]
                    dp[n][i - num] += dp[c][i]
        return dp[n][S + 1000]


if __name__ == "__main__":
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(Solution().findTargetSumWays([1, 2, 7, 9, 981], 1000000000))
