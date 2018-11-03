class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        p1, p2, b = n, 0, 1
        return (n - 1) // 10, (n - 10) // 100 * 10


if __name__ == "__main__":
    print(Solution().countDigitOne(13))
    print(Solution().countDigitOne(11))
    print(Solution().countDigitOne(111))
