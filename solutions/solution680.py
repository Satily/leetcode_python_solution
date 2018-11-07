class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def scan(s):
            ls = len(s)
            for i in range(ls // 2):
                if s[i] != s[ls - 1 - i]:
                    return i
            return None

        r = scan(s)
        if r is None:
            return True
        else:
            r1, r2 = scan(s[r: len(s) - 1 - r]), scan(s[r + 1: len(s) - r])
            if r1 is None or r2 is None:
                return True
            else:
                return False


if __name__ == "__main__":
    print(Solution().validPalindrome("aba"))
    print(Solution().validPalindrome("abca"))
