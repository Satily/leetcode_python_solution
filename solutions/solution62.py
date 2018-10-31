class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = m + n - 2
        n = n - 1
        if n * 2 > m:
            n = m - n
        r1 = 1
        r2 = 1
        for i in range(1, n + 1):
            r1 *= i
            r2 *= (m + 1 - i)
        return int(r2 / r1)


if __name__ == "__main__":
    print(Solution().uniquePaths(3, 2))
    print(Solution().uniquePaths(7, 3))
