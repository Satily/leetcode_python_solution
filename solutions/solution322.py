class Solution:
    def coinChange(self, coins: 'List[int]', amount: int) -> int:
        coins.sort(reverse=True)
        impossible = (amount + 1) * 2

        dp = [impossible] * (amount + 1)
        dp[0] = 0
        for current in range(amount + 1):
            for coin in coins:
                if current + coin <= amount:
                    dp[current + coin] = min(dp[current + coin], dp[current] + 1)

        return -1 if dp[amount] == impossible else dp[amount]


if __name__ == '__main__':
    print(Solution().coinChange([2], 4))
    print(Solution().coinChange([1, 2, 5], 11))
    print(Solution().coinChange([2], 3))
    print(Solution().coinChange([1], 0))
    print(Solution().coinChange([1], 1))
    print(Solution().coinChange([1], 2))
