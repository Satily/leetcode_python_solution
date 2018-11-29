import math


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        p = [True] * n
        p[0], p[1] = False, False
        for index in range(2, int(math.sqrt(n)) + 1):
            if p[index]:
                s = index * 2
                while s < n:
                    p[s] = False
                    s += index
        return sum(p)


if __name__ == "__main__":
    print(Solution().countPrimes(10))
    print(Solution().countPrimes(1))
    print(Solution().countPrimes(2))
    print(Solution().countPrimes(0))
    print(Solution().countPrimes(0))
    print(Solution().countPrimes(1500000))
