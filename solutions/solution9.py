class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        digits = []
        x2 = x
        while x2 > 0:
            digits.append(x2 % 10)
            x2 = x2 // 10
        for index, digit in enumerate(digits):
            if digits[len(digits) - 1 - index] != digit:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(-121))
    print(Solution().isPalindrome(10))
