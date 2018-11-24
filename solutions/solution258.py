class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1


if __name__ == "__main__":
    print(Solution().addDigits(38))
    print(Solution().addDigits(45))
