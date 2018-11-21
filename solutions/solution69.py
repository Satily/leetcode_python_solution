import math


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        epsl = 0.0001
        o = x
        o2 = o / 2 + x / o / 2
        while abs(o2 - o) > epsl:
            o = o2
            o2 = o / 2 + x / o / 2
        result = math.floor(o)
        if result * result > x:
            return result - 1
        else:
            return result


if __name__ == "__main__":
    print(Solution().mySqrt(4))
    print(Solution().mySqrt(1))
    print(Solution().mySqrt(2147395599))
