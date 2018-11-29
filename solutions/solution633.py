import math


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        squares = list(map(lambda x: x ** 2, range(int(math.sqrt(c)) + 1)))
        squares_set = set(squares)
        for square in squares:
            if (c - square) in squares_set:
                return True
        return False


if __name__ == "__main__":
    print(Solution().judgeSquareSum(5))
    print(Solution().judgeSquareSum(3))
