class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        times = 0
        while n > m:
            times += 1
            n >>= 1
            m >>= 1
        return m << times


if __name__ == "__main__":
    print(Solution().rangeBitwiseAnd(5, 7))
    print(Solution().rangeBitwiseAnd(0, 1))
