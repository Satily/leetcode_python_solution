class Solution:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_bin = []
        dp = [[1, 1]]
        while num > 0:
            num_bin.append(num & 1)
            dp.append([sum(dp[-1]), dp[-1][0]])
            num >>= 1
        return dp


if __name__ == "__main__":
    print(Solution().findIntegers(10000))
