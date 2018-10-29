class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        dp = [[False] * (lp + 1) for _ in range(0, ls + 1)]
        dp[0][0] = True
        for pi in range(0, lp):
            for si in range(0, )


if __name__ == "__main__":
    Solution().isMatch('aa', 'a')
    Solution().isMatch('aa', 'a*')
    Solution().isMatch('ab', '.*')
    Solution().isMatch('aab', 'c*a*b')
    Solution().isMatch('mississippi', 'mis*is*p*.')
