import math


# Time Limit for Python is TOOOOOOOOOOOOOOOO Short!!!!!
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_square(x):
            return int(math.sqrt(x)) ** 2 == x

        if is_square(n):
            return 1
        while n & 3 == 0:
            n >>= 2
        if n & 7 == 7:
            return 4
        for i in range(1, int(math.sqrt(n)) + 1):
            if is_square(n - i ** 2):
                return 2
        return 3


if __name__ == "__main__":
    print(Solution().numSquares(12))
    print(Solution().numSquares(13))
    print(Solution().numSquares(7168))
    print(Solution().numSquares(7217))
