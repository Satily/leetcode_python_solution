class Solution:
    def maxCoins(self, nums: 'List[int]') -> 'int':
        ln = len(nums)
        dp = [[0] * (ln + 1) for _ in range(ln + 1)]
        for l in range(1, ln + 1):
            for i in range(ln + 1 - l):
                s = 1
                if i - 1 != -1:
                    s *= nums[i - 1]
                if i + l != ln:
                    s *= nums[i + l]
                for k in range(l):
                    dp[i][l] = max(dp[i][l], dp[i][k] + dp[i + k + 1][l - k - 1] + s * nums[i + k])
        return dp[0][ln]


if __name__ == "__main__":
    print(Solution().maxCoins([3, 1, 5, 8]))
