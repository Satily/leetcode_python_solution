class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares5 = [5]
        while squares5[-1] < n:
            squares5.append(squares5[-1] * 5)
        return sum(map(lambda x: n // x, squares5))


if __name__ == "__main__":
    print(Solution().trailingZeroes(2))
    print(Solution().trailingZeroes(5))
    print(Solution().trailingZeroes(10))
