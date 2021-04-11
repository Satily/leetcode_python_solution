class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n & 3 != 0


if __name__ == "__main__":
    print(Solution().canWinNim(4))
