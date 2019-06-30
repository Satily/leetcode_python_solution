class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        lp = len(prices)
        if lp == 0:
            return 0

        lefts = []
        pivot = prices[0]
        max_diff = 0
        for p in prices:
            pivot = min(p, pivot)
            max_diff = max(max_diff, p - pivot)
            lefts.append(max_diff)

        rights = []
        pivot = prices[-1]
        max_diff = 0
        for p in reversed(prices):
            pivot = max(p, pivot)
            max_diff = max(max_diff, pivot - p)
            rights.append(max_diff)
        rights.reverse()

        result = [lefts[index] + rights[index] for index in range(lp)]
        return max(result)


if __name__ == "__main__":
    print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(Solution().maxProfit([1, 2, 3, 4, 5]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
