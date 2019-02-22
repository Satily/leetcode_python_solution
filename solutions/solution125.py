class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(lambda c: c.isalnum(), s.lower()))
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
    print(Solution().isPalindrome("0P"))
