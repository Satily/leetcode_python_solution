class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num % 4 == 0:
            num //= 4
        return num == 1


if __name__ == "__main__":
    print(Solution().isPowerOfFour(8))
