class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


if __name__ == "__main__":
    print(Solution().isPowerOfThree(177146))
    print(Solution().isPowerOfThree(27))
    print(Solution().isPowerOfThree(0))
    print(Solution().isPowerOfThree(9))
    print(Solution().isPowerOfThree(45))
