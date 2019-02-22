class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        result = 0
        left = prices[0]
        for index in range(1, len(prices)):
            if prices[index] < prices[index - 1]:
                result += prices[index - 1] - left
                left = prices[index]
        result += prices[-1] - left
        return result


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([1, 2, 3, 4, 5]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
