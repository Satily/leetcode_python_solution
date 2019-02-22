class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        primes = [2, 3, 5]
        for prime in primes:
            while num % prime == 0:
                num //= prime
        return num == 1


if __name__ == "__main__":
    print(Solution().isUgly(6))
    print(Solution().isUgly(8))
    print(Solution().isUgly(14))
