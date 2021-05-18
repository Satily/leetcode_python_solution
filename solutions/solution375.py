import sys


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        impossible = sys.maxsize
        dp = [[impossible] * (n + 1) for _ in range(n + 1)]
        for index in range(1, n + 1):
            dp[index][index] = 0
        for index in range(1, n):
            dp[index][index + 1] = index
        for length in range(3, n + 1):
            for index in range(1, n - length + 2):
                left, right = index, index + length - 1
                for mid in range(max(left + 1, (left + right) // 2), right):
                    dp[left][right] = min(dp[left][right], max(dp[left][mid - 1], dp[mid + 1][right]) + mid)
        return dp[1][n]


if __name__ == '__main__':
    print(Solution().getMoneyAmount(10))
    print(Solution().getMoneyAmount(1))
    print(Solution().getMoneyAmount(2))
